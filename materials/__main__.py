import argparse,json
from .physical import load_inventory
p=argparse.ArgumentParser(description="校验合成原始资料")
p.add_argument("path",nargs="?",default="inputs")
a=p.parse_args()
print(json.dumps(load_inventory(a.path),ensure_ascii=False,indent=2))
