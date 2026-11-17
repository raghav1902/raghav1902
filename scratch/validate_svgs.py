import os
import xml.etree.ElementTree as ET

assets_dir = r"C:\Users\ragha\OneDrive\Documents\GitHub\raghav1902\assets"
svg_files = [f for f in os.listdir(assets_dir) if f.endswith(".svg")]

print(f"Checking {len(svg_files)} SVGs in {assets_dir}...")
for fname in svg_files:
    fpath = os.path.join(assets_dir, fname)
    try:
        ET.parse(fpath)
        print(f"  [OK] {fname}")
    except ET.ParseError as e:
        print(f"  [ERROR] {fname}: {e}")
