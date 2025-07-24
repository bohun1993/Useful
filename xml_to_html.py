import xml.etree.ElementTree as ET


def xml_to_html(xml_file, html_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        with open(html_file, 'w') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>XML to HTML</title>\n</head>\n<body>\n')
            f.write('<h1>XML Content</h1>\n')
            f.write('<ul>\n')
            write_element_to_html(root, f)
            f.write('</ul>\n')
            f.write('</body>\n</html>')
        print(f"Converted '{xml_file}' to '{html_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def write_element_to_html(elem, file, indent=0):
    spaces = '  ' * indent
    file.write(f'{spaces}<li><strong>{elem.tag}</strong>')
    if elem.attrib:
        attr_str = ', '.join([f'{k}="{v}"' for k, v in elem.attrib.items()])
        file.write(f' <em>({attr_str})</em>')
    if elem.text and elem.text.strip():
        file.write(f': {elem.text.strip()}')
    file.write('</li>\n')

    if list(elem):
        file.write(f'{spaces}<ul>\n')
        for child in elem:
            write_element_to_html(child, file, indent + 1)
        file.write(f'{spaces}</ul>\n')


# Example usage
if __name__ == "__main__":
    xml_to_html('example.xml', 'output.html')
