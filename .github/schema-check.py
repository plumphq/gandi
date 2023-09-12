import json
import os
import yaml

has_errors = False


def check_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                check_json_file(os.path.join(root, file))
            elif file.endswith('.yaml'):
                check_yaml_file(os.path.join(root, file))


def check_json_file(json_path):
    global has_errors
    try:
        with open(json_path, 'r') as json_file:
            json.load(json_file)
    except ValueError as e:
        print(f'JSON file {json_path} is not valid. Please fix the syntax:\n {e}')
        has_errors = True


def check_yaml_file(yaml_path):
    global has_errors
    try:
        with open(yaml_path, 'r') as yaml_file:
            yaml.safe_load(yaml_file)
    except yaml.scanner.ScannerError as e:
        print(f'YAML file {yaml_path} is not valid. Please fix the syntax:\n {e}')
        has_errors = True


check_directory('careers')

if has_errors:
    exit(1)
