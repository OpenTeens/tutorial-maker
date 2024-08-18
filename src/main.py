import re
import importlib
import os
import markdown

with open("example.md") as f:
    raw_md = f.read()

# COMPONENT
TAG = "-" * 5
comp_num = raw_md.count(TAG) // 4
for i in range(comp_num):
    start = raw_md.find(TAG) + len(TAG)
    end = raw_md.find(TAG, start + 1)
    component_name = raw_md[start:end]

    start = raw_md.find(TAG, end) + len(TAG) + 1  # '\n' is also included
    end = raw_md.find(TAG, start + 1)
    component_content = raw_md[start:end]

    component_sections = re.split(r"\n{2,10}", component_content)
    component_sections = [section.strip() for section in component_sections]

    print(f"Component Name: {component_name}")
    print(f"Component Sections: {component_sections}")

    component_parser = importlib.import_module(f"components.{component_name}")

    parsed = component_parser.parse(component_sections)

    raw_md = raw_md.replace(f"{TAG}{component_name}{TAG}\n{component_content}{TAG}{component_name}{TAG}", parsed)


# ASSETS
assets_path = "src/assets"

css = ""
for fname in os.listdir(f"{assets_path}/style"):
    with open(f"{assets_path}/style/{fname}") as f:
        css += f.read()

js = ""
for fname in os.listdir(f"{assets_path}/script"):
    with open(f"{assets_path}/script/{fname}") as f:
        js += f.read()

# OUTPUT
html = markdown.markdown(raw_md)
with open("output.html", "w") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
        <style>{css}</style>
    </head>
    <body>
        <article class="markdown-body">
            {html}
        </article>
    </body>
    <script>{js}</script>
    </html>
    """)
