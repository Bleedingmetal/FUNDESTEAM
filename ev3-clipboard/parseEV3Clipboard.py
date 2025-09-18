import xml.etree.ElementTree as ET
import pyperclip
import re

def strip_namespace(tree):
    for elem in tree.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]
    return tree

def describe_ev3_clipboard():
    # read clipboard
    xml_text = pyperclip.paste()
    if not xml_text.strip():
        print("Clipboard is empty.")
        return

    # remove BOM and stray characters
    xml_text = xml_text.lstrip("\ufeff").strip()

    try:
        root = ET.fromstring(xml_text)
    except Exception as e:
        print(f"Could not parse clipboard XML: {e}")
        return

    root = strip_namespace(root)

    description_lines = []

    # Look for known block types
    for item in root.findall(".//MergeItem"):
        block = list(item)[0]  # e.g. StartBlock or ConfigurableMethodCall
        block_type = block.tag
        target = block.attrib.get("Target", "")
        description_lines.append(f"Block type: {block_type}")
        if target:
            description_lines.append(f"  Target: {target}")

        # Configurable terminals
        for term in block.findall(".//ConfigurableMethodTerminal"):
            config_val = term.attrib.get("ConfiguredValue")
            inner_term = term.find("Terminal")
            if inner_term is not None:
                tid = inner_term.attrib.get("Id", "")
                direction = inner_term.attrib.get("Direction", "")
                dtype = inner_term.attrib.get("DataType", "")
                if config_val is not None:
                    description_lines.append(f"  {tid} ({direction}, {dtype}) = {config_val}")
                else:
                    description_lines.append(f"  {tid} ({direction}, {dtype})")

        # Bare terminals
        for term in block.findall("Terminal"):
            tid = term.attrib.get("Id", "")
            direction = term.attrib.get("Direction", "")
            dtype = term.attrib.get("DataType", "")
            description_lines.append(f"  {tid} ({direction}, {dtype})")

    if description_lines:
        print("\n".join(description_lines))
    else:
        print("No recognizable EV3 block found in clipboard.")

if __name__ == "__main__":
    describe_ev3_clipboard()
