import json
from jsonschema import validate

class OSCALCatalogParser:
    def __init__(self, schema_path):
        with open(schema_path, 'r') as schema_file:
            self.schema = json.load(schema_file)

    def parse(self, json_data):
        try:
            validate(instance=json_data, schema=self.schema)
            # Parsing logic goes here
            # Extract relevant data from json_data according to the schema
            catalog_id = json_data.get('uuid', '')
            title = json_data.get('metadata', {}).get('title', '')
            # Example: Extracting controls
            controls = json_data.get('controls', [])
            control_ids = [control.get('id', '') for control in controls]
            return {
                'catalog_id': catalog_id,
                'title': title,
                'control_ids': control_ids
            }
        except Exception as e:
            print("Validation error:", e)

# Example usage
if __name__ == "__main__":
    schema_path = 'oscal_catalog_schema.json'
    parser = OSCALCatalogParser(schema_path)

    # Load JSON data
    with open('example_catalog.json', 'r') as json_file:
        json_data = json.load(json_file)

    parsed_data = parser.parse(json_data)
    print(parsed_data)
