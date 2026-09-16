import json
import yaml
import xmltodict
import os

def auto_read_config(file_path):
    """Task 1 & 3: Reads JSON, YAML, or XML with format auto-detection and error handling."""
    if not os.path.exists(file_path):
        print(f"\n[!] Error: File '{file_path}' does not exist.")
        return None
    
