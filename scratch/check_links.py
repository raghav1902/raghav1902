import re
import os

readme_path = r"C:\Users\ragha\OneDrive\Documents\GitHub\raghav1902\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all assets references
asset_refs = re.findall(r'assets/[\w\-\.]+\.svg', content)
print(f"Found {len(asset_refs)} asset references:")
for ref in set(asset_refs):
    full_path = os.path.join(r"C:\Users\ragha\OneDrive\Documents\GitHub\raghav1902", ref.replace("/", "\\"))
    exists = os.path.exists(full_path)
    print(f"  {ref} -> Exists: {exists}")
