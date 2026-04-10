import yaml

with open("README.yaml") as f:
    data = yaml.safe_load(f)

badges = "\n".join(
    [f"[![{b['name']}]({b['image']})]({b['url']})" for b in data.get("badges", [])]
)

prereq = "\n".join(
    [f"- {p['name']} ({p['version']})" for p in data.get("prerequesties", [])]
)

providers = "\n".join(
    [f"- {p['name']} ({p['version']})" for p in data.get("providers", [])]
)

readme = f"""# {data.get('name', '')}

{badges}

## Description
{data.get('description', '')}

## Prerequisites
{prereq}

## Providers
{providers}

## Usage
{data.get('usage', '')}

---

<!-- BEGIN_TF_DOCS -->
<!-- END_TF_DOCS -->
"""

with open("README.md", "w") as f:
    f.write(readme)