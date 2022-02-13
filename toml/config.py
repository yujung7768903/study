from os import path
from pathlib import Path
import toml
from tomlkit import dump, load

cfg_path = './config.toml'

# 파일 수정하기
def update_config():
    with open(cfg_path, 'r') as f:
        data = load(f)
    with open(f'{cfg_path}.bak', 'w') as f: # Create backup file
        dump(data, f)
    data["owner"]["name"] = "yujung"
    with open(cfg_path, 'w') as f:
        dump(data, f)

update_config()


    
# config_data = toml.load("./config2.toml")
# config_data["agent"]["scaling-group"] = "HPC"
# f = open("./config2.toml", "w")
# toml.dump(config_data, f)
# f.close()

# doc = tomlkit.document()
# doc["test"] = {"name": "test"}
# path.write(doc)

