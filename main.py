import json
import yaml
from yaml.loader import SafeLoader

def parse_json():
    with open('app.yaml', 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
    print(type(data['ABC']))
    return

if __name__ == "__main__":
    parse_json()