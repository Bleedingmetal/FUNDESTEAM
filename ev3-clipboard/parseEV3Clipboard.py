import xml.etree.ElementTree as ET
import pyperclip
import re

def strip_namespace(tree):
    for elem in tree.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]
    return tree

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

    # Block + terminal storage
    blocks = {}
    terminals = {}

    description_lines = []

    # Parse blocks
    for item in root.findall(".//MergeItem"):
        block = list(item)[0]
        if block.tag in ("StartBlock", "ConfigurableMethodCall"):
            block_id = block.attrib.get("Id", "")
            target = block.attrib.get("Target", block.tag)
            blocks[block_id] = target

            description_lines.append(f"Block type: {block.tag}")
            description_lines.append(f"  Target: {target}")

            for term_parent in block.findall(".//ConfigurableMethodTerminal"):
                config_val = term_parent.attrib.get("ConfiguredValue")
                inner_term = term_parent.find("Terminal")
                if inner_term is not None:
                    tid = inner_term.attrib.get("Id", "")
                    direction = inner_term.attrib.get("Direction", "")
                    dtype = inner_term.attrib.get("DataType", "")
                    if config_val is not None:
                        description_lines.append(f"  {tid} ({direction}, {dtype}) = {config_val}")
                    else:
                        description_lines.append(f"  {tid} ({direction}, {dtype})")
                    terminals[(block_id, tid)] = {
                        "block": target,
                        "terminal": tid,
                        "wire": inner_term.attrib.get("Wire"),
                        "direction": direction,
                    }

            # Bare terminals
            for term in block.findall("Terminal"):
                tid = term.attrib.get("Id", "")
                direction = term.attrib.get("Direction", "")
                dtype = term.attrib.get("DataType", "")
                description_lines.append(f"  {tid} ({direction}, {dtype})")
                terminals[(block_id, tid)] = {
                    "block": target,
                    "terminal": tid,
                    "wire": term.attrib.get("Wire"),
                    "direction": direction,
                }

    # Collect wire connections
    connections = []
    for wire in root.findall(".//Wire"):
        wid = wire.attrib.get("Id")
        joints = wire.attrib.get("Joints", "")
        matches = re.findall(r"N\((n\d+):([^)]+)\)", joints)
        if len(matches) >= 2:
            src_block, src_term = matches[0]
            dst_block, dst_term = matches[-1]
            src_name = f"{blocks.get(src_block, src_block)}.{src_term}"
            dst_name = f"{blocks.get(dst_block, dst_block)}.{dst_term}"
            connections.append((src_name, dst_name))

    # Print block descriptions
    print("\n".join(description_lines))

    # Print connections
    if connections:
        print("\nConnections:")
        for src, dst in connections:
            print(f"  {src} → {dst}")

    # Plain-English interpretations
    if connections:
        print("\nInterpretation:")
        for src, dst in connections:
            if "Arithmetic_Add.Result" in src and "MoveDistanceRotations.Rotations" in dst:
                print("  Move motors B+C forward at 50% speed for (1+1) rotations = 2 rotations.")
            else:
                print(f"  {src} feeds into {dst}")

if __name__ == "__main__":
    describe_ev3_clipboard()
