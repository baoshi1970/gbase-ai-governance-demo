from pathlib import Path

root = Path(__file__).resolve().parent
page = root / "index.html"
html = page.read_text(encoding="utf-8")
prefix, tail = html.split("<script>", 1)
_, suffix = tail.rsplit("</script>", 1)
source = (root / "governance.js").read_text(encoding="utf-8")
page.write_text(prefix + "<script>\n" + source.rstrip() + "\n</script>" + suffix, encoding="utf-8")
print("Updated index.html from governance.js")
