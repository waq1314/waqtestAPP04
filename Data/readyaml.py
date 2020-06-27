import yaml
with open("./data2.yml","r",encoding="utf-8")as f:
    data=yaml.safe_load(f)
    print(data)
