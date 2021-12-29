from os import path
from pathlib import Path
import toml
from tomlkit import dump, load

def update_config():
    with open('./config.toml', 'r') as f:
        data = load(f)
        data["agent"]["scaling-group"] = "HPC"
    with open('./config.toml', 'w') as f:
        dump(data, f)

update_config()
    
config_data = toml.load("./config2.toml")
config_data["agent"]["scaling-group"] = "HPC"
f = open("./config2.toml", "w")
toml.dump(config_data, f)
f.close()

# doc = tomlkit.document()
# doc["test"] = {"name": "test"}
# path.write(doc)

