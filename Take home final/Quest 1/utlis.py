import os

def make_folder(path):
    os.makedirs(path, exist_ok=True)

def file_exists(xml_path, json_path):
    return os.path.exists(xml_path) and os.path.exists(json_path)
