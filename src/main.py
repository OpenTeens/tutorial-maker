import re
import importlib
import os

import markdown
import jinja2

with open("example.md") as f:
    raw_md = f.read()

# COMPONENT
TAG = "-" * 5
comp_num = raw_md.count(TAG) // 4

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("src/components/template"))

for i in range(comp_num):
    # read
    start = raw_md.find(TAG) + len(TAG)
    end = raw_md.find(TAG, start + 1)
    component_name = raw_md[start:end].lower()

    start = raw_md.find(TAG, end) + len(TAG) + 1  # '\n' is also included
    end = raw_md.find(TAG, start + 1)
    component_content = raw_md[start:end]

    component_full = f"{TAG}{component_name}{TAG}\n{component_content}{TAG}{component_name}{TAG}"

    # process
    component_sections = re.split(r"\n{2,10}", component_content)
    component_sections = [section.strip() for section in component_sections]

    component_id = hex(hash(component_name + component_content))[2:]
    comp_id = f"comp-{component_name}-{component_id}"

    # custom preprocess
    module = importlib.import_module(f"components.script.{component_name}")
    component_vars = module.process(component_sections, comp_id)

    # render
    template = environment.get_template(f"{component_name}.html")
    component_html = template.render(**component_vars, sections=component_sections, comp_id=comp_id)
    
    # replace
    raw_md = raw_md.replace(component_full, component_html)


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
        <script>{js}</script>
    </html>
    </head>
    <body>
        <article class="markdown-body">
            {html}
        </article>
    </body>
    """)
