import xml.etree.ElementTree as ET
import pyperclip

def strip_namespace(tree):
    for elem in tree.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]
    return tree

def format_attrs(attrs):
    """Format all attributes as key=value pairs"""
    return " ".join([f'{k}="{v}"' for k, v in attrs.items()])

def describe_ev3_clipboard():
    xml_text = pyperclip.paste()
    if not xml_text.strip():
        print("Clipboard is empty.")
        return

    xml_text = xml_text.lstrip("\ufeff").strip()

    try:
        root = ET.fromstring(xml_text)
    except Exception as e:
        print(f"Could not parse clipboard XML: {e}")
        return

    root = strip_namespace(root)

    # Pass 1: Blocks
    for item in root.findall(".//MergeItem"):
        block = list(item)[0]
        if block.tag in ("StartBlock", "ConfigurableMethodCall"):
            target = block.attrib.get("Target", block.tag)
            print(f"Target: {target}")
            print(f"  Attributes: {format_attrs(block.attrib)}")

            # Configurable terminals
            for term_parent in block.findall(".//ConfigurableMethodTerminal"):
                print(f"  ConfigurableMethodTerminal: {format_attrs(term_parent.attrib)}")
                inner_term = term_parent.find("Terminal")
                if inner_term is not None:
                    print(f"    Terminal: {format_attrs(inner_term.attrib)}")

            # Bare terminals
            for term in block.findall("Terminal"):
                print(f"  Terminal: {format_attrs(term.attrib)}")

            print("")

    # Pass 2: Wires
    for wire in root.findall(".//Wire"):
        wid = wire.attrib.get("Id")
        print(f"Wire: {wid}")
        print(f"  Attributes: {format_attrs(wire.attrib)}")
        print("")

if __name__ == "__main__":
    describe_ev3_clipboard()
