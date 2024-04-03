from lxml import etree

class OSCALCatalogParser:
    def __init__(self):
        pass  # Assuming schema validation is handled separately or not required for parsing

    def parse(self, xml_data_path):
        ns = {'oscal': 'http://csrc.nist.gov/ns/oscal/1.0'}
        
        try:
            tree = etree.parse(xml_data_path)
            root = tree.getroot()

            catalog_id = root.attrib['uuid']
            title = root.find('oscal:metadata/oscal:title', ns).text
            
            controls = root.findall('.//oscal:control', ns)
            control_details = []
            for control in controls:
                control_id = control.get('id')
                control_title = control.find('oscal:title', ns).text if control.find('oscal:title', ns) is not None else "No Title"
                
                # Assuming statements are contained within 'oscal:part' elements with a 'name' attribute of 'statement'
                statements = control.findall("oscal:part[@name='statement']", ns)
                statement_texts = []
                for statement in statements:
                    # Each 'oscal:part' may contain multiple 'oscal:part' elements representing different statement items
                    parts = statement.findall("oscal:part", ns)
                    for part in parts:
                        if part.text:
                            statement_texts.append(part.text.strip())
                
                control_details.append({
                    'id': control_id,
                    'title': control_title,
                    'statements': statement_texts
                })

            return {
                'catalog_id': catalog_id,
                'title': title,
                'controls': control_details
            }
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
