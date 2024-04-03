from oscal_catalog_parser import OSCALCatalogParser

def main():
    # Path to the OSCAL catalog XML file
    xml_file_path = 'catalogs/NIST_SP-800-53_rev5_catalog.xml'

    # Initialize the parser without schema_path
    parser = OSCALCatalogParser()

    # Parse the XML data
    parsed_data = parser.parse(xml_file_path)

    # Display the parsed data
    if parsed_data:
        print("Catalog ID:", parsed_data['catalog_id'])
        print("Title:", parsed_data['title'])
        
        # Iterate through the controls and print details
        for control in parsed_data['controls']:
            print("\nControl ID:", control['id'])
            print("Title:", control['title'])
            
            # Print prose if available
            if 'prose' in control:
                print("Prose:", control['prose'])
                
            # Print statements if available
            if 'statements' in control:
                print("Statements:")
                for statement_text in control['statements']:
                    print(f"  {statement_text}")
            else:
                print("No statements available.")

    else:
        print("Failed to parse the OSCAL catalog.")

if __name__ == "__main__":
    main()
