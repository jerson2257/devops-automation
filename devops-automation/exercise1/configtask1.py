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

def create_combined_inventory():
    """Task 4: Generates a combined inventory file in JSON, YAML, and XML formats."""
    combined_inventory = {
        "inventory": {
            "devices": [
                {"name": "router-01", "type": "router", "ip": "192.168.1.1", "status": "active"},
                {"name": "switch-01", "type": "switch", "ip": "192.168.1.2", "status": "active"},
                {"name": "fw-01", "type": "firewall", "ip": "192.168.1.20", "status": "maintenance"}
            ]
        }
    }
    try:
        with open('combined_inventory.json', 'w') as f:
            json.dump(combined_inventory, f, indent=4)
        with open('combined_inventory.yaml', 'w') as f:
            yaml.dump(combined_inventory, f, default_flow_style=False, indent=2)
        with open('combined_inventory.xml', 'w') as f:
            f.write(xmltodict.unparse(combined_inventory, pretty=True))
        print("\n[+] Success: Created combined_inventory.json, .yaml, and .xml")
    except Exception as err:
        print(f"\n[!] Failed to create combined inventory: {err}")

def main():
    while True:
        print("\n" + "=" * 40)
        print("   DevOps Config Manager CLI Tool")
        print("=" * 40)
        print("1. Read & Display Any Config File (JSON/YAML/XML)")
        print("2. Convert File Format (Any to Any)")
        print("3. Generate Combined Inventory in All 3 Formats")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            path = input("Enter file path to read (e.g., network_devices.json): ").strip()
            data = auto_read_config(path)
            if data is not None:
                print("\n--- File Content Output ---")
                print(json.dumps(data, indent=2))
                
        elif choice == '2':
            src = input("Enter source file path (e.g., ansible_inventory.yaml): ").strip()
            dst = input("Enter target file path (e.g., ansible_inventory.json): ").strip()
            convert_format(src, dst)
            
        elif choice == '3':
            create_combined_inventory()
            
        elif choice == '4':
            print("Exiting tool...")
            break
            
        else:
            print("[!] Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()