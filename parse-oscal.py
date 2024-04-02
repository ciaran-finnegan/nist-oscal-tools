import json
from oscal_catalog_parser import OSCALCatalogParser



def main():
    # Path to the OSCAL catalog schema
    schema_path = 'schemas/oscal_catalog_schema.json'
    
    # Initialize the parser
    parser = OSCALCatalogParser(schema_path)

    # Path to the OSCAL catalog JSON file
    json_file_path = 'catalogs/NIST_SP-800-53_rev5_catalog.json'

    # Load JSON data
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Parse the JSON data
    parsed_data = parser.parse(json_data)

    # Display the parsed data
    if parsed_data:
        print("Catalog ID:", parsed_data['catalog_id'])
        print("Title:", parsed_data['title'])
        print("Control IDs:", parsed_data['control_ids'])
    else:
        print("Failed to parse the OSCAL catalog.")

if __name__ == "__main__":
    main()
