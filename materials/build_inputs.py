import hashlib,json
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq

def main():
    root=Path(__file__).resolve().parents[1]/"inputs"
    seed=json.loads((root/"seed.json").read_text(encoding="utf-8"))
    for name,rows in seed.items():
        table=pa.Table.from_pylist(rows)
        pq.write_table(table,root/(name+".parquet"),row_group_size=2,compression="zstd")
    files=[]
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name=="inventory.json":continue
        data=p.read_bytes();item={"path":p.relative_to(root).as_posix(),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
        if p.suffix==".parquet":item["rows"]=pq.ParquetFile(p).metadata.num_rows
        files.append(item)
    (root/"inventory.json").write_text(json.dumps({"files":files},ensure_ascii=False,indent=2),encoding="utf-8")
    print("已生成输入物理文件",len(files))
if __name__=="__main__":main()
