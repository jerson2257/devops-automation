import json
import yaml
import xmltodict
import os

def auto_read_config(file_path):
    if not os.path.exists(file_path):
        print(f"\n[!] Error: File '{file_path}' does not exist.")
        return None
    
    ext = os.path.splitext(file_path)[1].lower()
    
    try:
        with open(file_path, 'r') as file:
            if ext == '.json':
                return json.load(file)
            elif ext in ['.yaml', '.yml']:
                return yaml.safe_load(file)
            elif ext == '.xml':
                return xmltodict.parse(file.read())
            else:
                print(f"\n[!] Error: Unsupported file format '{ext}'.")
                return None
    except (json.JSONDecodeError, yaml.YAMLError) as parse_err:
        print(f"\n[!] Syntax/Parsing error in '{file_path}': {parse_err}")
    except Exception as err:
        print(f"\n[!] Unexpected error reading file: {err}")
    return None

def convert_format(input_path, output_path):
    """Task 2 & 3: Converts any supported file format to another format."""
    data = auto_read_config(input_path)
    if data is None:
        return False
    
    out_ext = os.path.splitext(output_path)[1].lower()
    
    try:
        with open(output_path, 'w') as file:
            if out_ext == '.json':
                json.dump(data, file, indent=4)
            elif out_ext in ['.yaml', '.yml']:
                yaml.dump(data, file, default_flow_style=False, indent=2)
            elif out_ext == '.xml':
                file.write(xmltodict.unparse(data, pretty=True))
            else:
                print(f"\n[!] Error: Target format '{out_ext}' is unsupported.")
                return False
                
        print(f"\n[+] Success: Converted '{input_path}' -> '{output_path}'")
        return True
    except Exception as err:
        print(f"\n[!] Failed to write converted output: {err}")
        return False

