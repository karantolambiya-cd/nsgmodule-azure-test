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


# import yaml

# with open("README.yaml") as f:
#     data = yaml.safe_load(f)

# # Banner
# banner = ""
# if data.get("banner"):
#     banner = f"""
# <p align="center">
#   <a href="{data['banner']['link']}">
#     <img src="{data['banner']['image']}" alt="Banner" />
#   </a>
# </p>
# """

# # Table for prerequisites/providers
# table = ""
# if data.get("prerequisites_table"):
#     table = "## Prerequisites and Providers\n\n"
#     table += "| Description | Name | Version |\n"
#     table += "|-------------|------|---------|\n"
#     for item in data["prerequisites_table"]:
#         table += f"| {item['type']} | {item['name']} | {item['version']} |\n"

# readme = f"""
# {banner}

# # {data.get('title', '')}

# {data.get('intro', '')}

# {data.get('badges_text', '')}

# ---

# {data.get('about', '')}

# ---

# {table}

# ---

# ## 📌 Examples
# Check examples/ directory.

# ---

# ## 📥 Inputs and Outputs

# Refer to complete documentation below.

# <!-- BEGIN_TF_DOCS -->
# <!-- END_TF_DOCS -->

# ---

# {data.get('extras', '')}
# """

# with open("README.md", "w") as f:
#     f.write(readme)