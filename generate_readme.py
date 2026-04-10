import yaml
 
 
def anchor(name):
    """Generate a GitHub markdown anchor id from a variable name."""
    return name.replace("_", "\\_")
 
 
def build_requirements_table(data):
    """Build the Requirements table from prerequesties."""
    rows = data.get("prerequesties") or []
    if not rows:
        return ""
    lines = [
        "## Requirements\n",
        "| Name | Version |",
        "|------|---------|",
    ]
    for r in rows:
        name = r["name"]
        ver = r.get("version", "")
        anchor_id = name.lower().replace(" ", "_")
        lines.append(
            f'| <a name="requirement_{anchor_id}"></a> [{anchor(name)}](#{anchor_id}) | {ver} |'
        )
    return "\n".join(lines)
 
 
def build_providers_table(data):
    """Build the Providers table."""
    rows = data.get("providers") or []
    if not rows:
        return ""
    lines = [
        "## Providers\n",
        "| Name | Version |",
        "|------|---------|",
    ]
    for p in rows:
        name = p["name"]
        ver = p.get("version", "")
        anchor_id = name.lower().replace(" ", "_")
        lines.append(
            f'| <a name="provider_{anchor_id}"></a> [{anchor(name)}](#{anchor_id}) | {ver} |'
        )
    return "\n".join(lines)
 
 
def build_modules_table(data):
    """Build the Modules table."""
    rows = data.get("modules") or []
    if not rows:
        return ""
    lines = [
        "## Modules\n",
        "| Name | Source | Version |",
        "|------|--------|---------|",
    ]
    for m in rows:
        name = m["name"]
        source = m.get("source", "")
        ver = m.get("version", "")
        anchor_id = f"module_{name.lower()}"
        lines.append(
            f'| <a name="{anchor_id}"></a> [{name}](#{anchor_id}) | {source} | {ver} |'
        )
    return "\n".join(lines)
 
 
def build_resources_table(data):
    """Build the Resources table."""
    rows = data.get("resources") or []
    if not rows:
        return ""
    lines = [
        "## Resources\n",
        "| Name | Type |",
        "|------|------|",
    ]
    for r in rows:
        name = r["name"]
        rtype = r.get("type", "resource")
        url = r.get("url", "#")
        lines.append(f"| [{name}]({url}) | {rtype} |")
    return "\n".join(lines)
 
 
def build_inputs_table(data):
    """Build the Inputs table with name, description, type, default, required."""
    rows = data.get("inputs") or []
    if not rows:
        return ""
    lines = [
        "## Inputs\n",
        "| Name | Description | Type | Default | Required |",
        "|------|-------------|------|---------|:--------:|",
    ]
    for inp in rows:
        name = inp["name"]
        desc = (inp.get("description") or "").replace("\n", " ").replace("|", "\\|")
        raw_type = (inp.get("type") or "string").strip()
        required = inp.get("required", False)
        default_val = inp.get("default")
 
        # Format multi-line types as a code block
        if "\n" in raw_type:
            formatted_type = "<pre>" + raw_type.replace("\n", "<br/>").replace("  ", "&nbsp;&nbsp;") + "</pre>"
        else:
            formatted_type = f"`{raw_type}`"
 
        # Format default value
        if required or default_val is None:
            formatted_default = "n/a"
            req_symbol = "yes"
        else:
            default_str = str(default_val).strip() if default_val != "~" else "null"
            formatted_default = f"`{default_str}`"
            req_symbol = "no"
 
        anchor_id = f"input_{name}"
        lines.append(
            f'| <a name="{anchor_id}"></a> [{anchor(name)}](#{anchor_id}) '
            f"| {desc} | {formatted_type} | {formatted_default} | {req_symbol} |"
        )
    return "\n".join(lines)
 
 
def build_outputs_table(data):
    """Build the Outputs table."""
    rows = data.get("outputs") or []
    if not rows:
        return ""
    lines = [
        "## Outputs\n",
        "| Name | Description |",
        "|------|-------------|",
    ]
    for out in rows:
        name = out["name"]
        desc = (out.get("description") or "").replace("|", "\\|")
        anchor_id = f"output_{name}"
        lines.append(
            f'| <a name="{anchor_id}"></a> [{anchor(name)}](#{anchor_id}) | {desc} |'
        )
    return "\n".join(lines)
 
 
def generate_readme(yaml_path="README.yaml", output_path="README.md"):
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
 
    # ── Simple string fields ──────────────────────────────────────────────────
    name         = (data.get("name") or "").strip()
    intro        = (data.get("intro") or "").strip()
    badges_text  = (data.get("badges_text") or "").strip()
    about        = (data.get("about") or "").strip()
    description  = (data.get("description") or "").strip()
    usage        = (data.get("usage") or "").strip()
    extras       = (data.get("extras") or "").strip()
 
    # ── Badges (inline) ───────────────────────────────────────────────────────
    badges = " ".join(
        f"[![{b['name']}]({b['image']})]({b['url']})"
        for b in (data.get("badges") or [])
    )
 
    # ── Prerequisites + Providers (summary table at top) ─────────────────────
    prereq_rows = []
    for p in (data.get("prerequesties") or []):
        prereq_rows.append(f"| Prerequisite | {p['name']} | {p['version']} |")
    for p in (data.get("providers") or []):
        prereq_rows.append(f"| Provider | {p['name']} | {p['version']} |")
 
    if prereq_rows:
        prereq_summary = (
            "| Description | Name | Version |\n"
            "|-------------|------|---------|\n"
            + "\n".join(prereq_rows)
        )
    else:
        prereq_summary = "_No prerequisites or providers defined._"
 
    # ── Detailed terraform-docs style tables ─────────────────────────────────
    tf_docs_sections = "\n\n".join(filter(None, [
        build_requirements_table(data),
        build_providers_table(data),
        build_modules_table(data),
        build_resources_table(data),
        build_inputs_table(data),
        build_outputs_table(data),
    ]))
 
    tf_docs_block = (
        "<!-- BEGIN_TF_DOCS -->\n"
        + tf_docs_sections
        + "\n<!-- END_TF_DOCS -->"
    )
 
    # ── Assemble sections, skip empties ──────────────────────────────────────
    parts = [
        f"# {name}",
        intro,
        badges_text,
        badges,
        "---",
        "## 📖 About",
        about,
        "---",
        "## ⚙️ Prerequisites and Providers",
        prereq_summary,
        "---",
        "## 📝 Description",
        description,
        "---",
        "## 🚀 Usage",
        usage,
        "---",
        "## 📥 Inputs and Outputs",
        tf_docs_block,
        "---",
    ]
 
    if extras:
        parts.append(extras)
 
    readme = "\n\n".join(p for p in parts if p) + "\n"
 
    with open(output_path, "w") as f:
        f.write(readme)
 
    print(f"✅  {output_path} generated successfully.")
 
 
if __name__ == "__main__":
    generate_readme()
 