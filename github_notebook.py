import json
from pathlib import Path

notebook_path = Path("Lab_Week6_PathVQA_GPT_LoRA.ipynb")  # change this

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Remove problematic top-level widget metadata
if "metadata" in nb and "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

# Optional: remove widget-related metadata inside cells, keep outputs untouched
for cell in nb.get("cells", []):
    metadata = cell.get("metadata", {})
    metadata.pop("widgets", None)
    metadata.pop("colab", None)  # optional, usually safe for GitHub rendering

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("widgets still exists?", "widgets" in nb.get("metadata", {}))
print("outputs kept?", any(cell.get("outputs") for cell in nb.get("cells", [])))