"""合成输入的物理检查，不作统计推断或业务判断。"""
import hashlib,json
from pathlib import Path
import pyarrow.parquet as pq
import duckdb

def load_inventory(root):
    root=Path(root).resolve()
    inv=json.loads((root/"inventory.json").read_text(encoding="utf-8"))
    results=[]
    for entry in inv["files"]:
        raw=entry["path"]
        p=(root/raw).resolve()
        if not p.is_relative_to(root) or raw.startswith(("/", "\\")):
            raise ValueError("原件路径超出资料范围")
        data=p.read_bytes()
        if hashlib.sha256(data).hexdigest()!=entry["sha256"] or len(data)!=entry["bytes"]:
            raise ValueError("原件摘要或大小不符: "+raw)
        item={"path":raw,"bytes":len(data)}
        if p.suffix==".parquet":
            meta=pq.ParquetFile(p)
            if meta.metadata.num_rows!=entry["rows"]:raise ValueError("行数不符")
            with duckdb.connect() as con:
                count=con.execute("select count(*) from read_parquet(?)",[str(p)]).fetchone()[0]
            if count!=entry["rows"]:raise ValueError("物理读取行数不符")
            item["rows"]=count
        results.append(item)
    return results
