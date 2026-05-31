# Cover Letter Skill Entry Point

Use this skill when the user wants a tailored cover letter or lettre de motivation for an internship, alternance, job, or academic program.

## Prompt Schema

```text
@lettre
type: stage | alternance | poste | formation
langue: fr | en
spécialités: [comma-separated from: AI/LLM/RAG, data_science, mlops, computer_vision, big_data, nlp, full_stack]
cible: [URL or pasted description]
ton: (optional) formel | enthousiaste | sobre
notes: (optional) free text
```

## Execution Rules

1. Read `master_cv/sami_malek_master.html` and `master_cv/sami_malek_master_fr.html` as the master source material.
2. Read `specialty_mapping.md` and select the experiences/projects that best match the requested `spécialités`.
3. Choose the template that matches both `type` and `langue`:
   - `templates/formation_fr.md`
   - `templates/formation_en.md`
   - `templates/stage_fr.md`
   - `templates/stage_en.md`
   - `templates/alternance_fr.md`
   - `templates/alternance_en.md`
   - `templates/poste_fr.md`
   - `templates/poste_en.md`
4. Analyze `cible` as either a URL or a pasted description and extract:
   - expected profile;
   - technical focus;
   - institution/company signals;
   - strategic keywords;
   - any research, product, or business angle worth mirroring.
5. Use `ton` and `notes` only as calibration layers; never fabricate experience.

## Generation Instructions

Produce two deliverables every time:

### 1. Full Letter
- Ready to send.
- Respect the language and formatting rules from the chosen template.
- Prioritize concrete proof points, quantified impact, and truthful alignment.
- Keep the body concise and targeted.

### 2. Strategic Note
Add a short note after the letter that explains:
- which angle was prioritized;
- which experiences were selected from `specialty_mapping.md` and why;
- any gap that was acknowledged or reframed;
- any suggested personalization before sending.

## Quality Bar

- Mirror the target's vocabulary without sounding generic.
- Lead with value, not with a bland application formula.
- Keep the letter credible, specific, and evidence-based.
- Prefer 2-3 strong examples over a long list of projects.
