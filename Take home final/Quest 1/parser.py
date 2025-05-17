import xmltodict
import json

def xml_to_json(xml_path):
    if xml_path is None:
        return

    json_path = xml_path.replace(".xml", ".json")
    try:
        with open(xml_path, "r", encoding="utf-8") as f:
            xml_data = f.read()
        data_dict = xmltodict.parse(xml_data)
        with open(json_path, "w", encoding="utf-8") as f_json:
            json.dump(data_dict, f_json, indent=4)
        print(f"Converted to JSON: {json_path}")
    except Exception as e:
        print(f"Parsing failed for {xml_path}: {e}")