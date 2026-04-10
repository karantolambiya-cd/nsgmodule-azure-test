import yaml

with open("README.yaml") as f:
    data = yaml.safe_load(f)

# -------- Sections -------- #

intro = data.get("intro", "").strip()
about = data.get("about", "").strip()
badges_text = data.get("badges_text", "").strip()
description = data.get("description", "").strip()
usage = data.get("usage", "").strip()
extras = data.get("extras", "").strip()

# Badges (inline)
badges = " ".join(
    [f"[![{b['name']}]({b['image']})]({b['url']})" for b in data.get("badges", [])]
)

# Prerequisites table
prereq_table = ""
if data.get("prerequesties"):
    prereq_table += "| Description | Name | Version |\n"
    prereq_table += "|-------------|------|---------|\n"
    for p in data["prerequesties"]:
        prereq_table += f"| Prerequisite | {p['name']} | {p['version']} |\n"

# Providers table
if data.get("providers"):
    for p in data["providers"]:
        prereq_table += f"| Provider | {p['name']} | {p['version']} |\n"

# -------- README -------- #

readme = f"""# {data.get('name', '')}

{intro}

{badges_text}

{badges}

---

## 📖 About

{about}

---

## ⚙️ Prerequisites and Providers

{prereq_table}

---

## 📝 Description

{description}

---

## 🚀 Usage

{usage}

---

## 📥 Inputs and Outputs

<!-- BEGIN_TF_DOCS -->
<!-- END_TF_DOCS -->

---

{extras}
"""

with open("README.md", "w") as f:
    f.write(readme)