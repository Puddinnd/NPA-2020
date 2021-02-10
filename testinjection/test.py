from yaml import *

yaml_str = """!!python/object/apply:subprocess.Popen
- id"""
yaml_document = load(yaml_str, Loader=Loader)
print(yaml_document)
