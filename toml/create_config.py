from tomlkit import comment, dump, document, nl, table

cfg_path = './config2.toml'

# 파일 만들기
def create_config():
    doc = document()
    doc.add(comment("This is a TOML document."))
    doc.add(nl())
    doc.add("title", "TOML Example")

    owner = table()
    owner.add("name", "Tom Preston-Werner")
    owner.add("organization", "GitHub")
    owner["organization"].comment("주석 보존 확인")

    doc.add("owner", owner)

    database = table()
    database["server"] = "192.168.1.1"
    database["ports"] = [8001, 8001, 8002]
    database["connection_max"] = 5000
    database["enabled"] = True

    doc["database"] = database

    with open(cfg_path, "w") as f:
        dump(doc, f)

create_config()