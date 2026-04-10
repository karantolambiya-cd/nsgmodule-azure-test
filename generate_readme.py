import yaml

with open("README.yaml") as f:
    data = yaml.safe_load(f)

# -------- Sections -------- #

intro = data.get("intro", "").strip()
about = data.get("about", "").strip()
badges_text = data.get("badges_text", "").strip()

# Badges
badges = " ".join(
    [f"[![{b['name']}]({b['image']})]({b['url']})" for b in data.get("badges", [])]
)

# Prerequisites
prereq = "\n".join(
    [f"- **{p['name']}** ({p['version']})" for p in data.get("prerequesties", [])]
)

# Providers
providers = "\n".join(
    [f"- **{p['name']}** ({p['version']})" for p in data.get("providers", [])]
)

# Extras
extras = data.get("extras", "").strip()

# -------- README -------- #

readme = f"""# {data.get('name', '')}

{intro}

{badges_text}

{badges}

---

## 📖 About

{about}

---

## ⚙️ Prerequisites

{prereq}

## 🔌 Providers

{providers}

---

## 📝 Description

{data.get('description', '').strip()}

---

## 🚀 Usage

{data.get('usage', '').strip()}

---

## 📥 Inputs and Outputs

<!-- BEGIN_TF_DOCS -->
<!-- END_TF_DOCS -->

---

{extras}
"""

# -------- Write file -------- #

with open("README.md", "w") as f:
    f.write(readme)