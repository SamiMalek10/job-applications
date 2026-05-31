# Job Application Automation Skill System

Use this as the main orchestrator for `@cv` and `@lettre` requests.

## 1) Trigger Prompt Format

```txt
type: stage | alternance | poste | formation
langue: fr | en | both
spécialités: [comma-separated from: AI/LLM/RAG, data_science, big_data, computer_vision, mlops, nlp, full_stack, iot]
cible: [URL or pasted job description]
ton: (optional) formel | enthousiaste | sobre
notes: (optional) free text
output: cv | lettre | both
```

## 2) Decision Logic

1. Parse `type`, `langue`, `spécialités`, `cible`, `ton`, `notes`, `output`.
2. Load template:
   - `templates/{type}_{langue}.md`
   - If `langue: both`, run twice (`fr` then `en`) with matching templates.
3. Load `specialty_mapping.md` and select only relevant experiences/projects/skills based on selected specialties.
4. Use source-of-truth profile data from:
   - `cv/sami_malek_master_en.html`
   - `cv/sami_malek_master_fr.html`
5. Route generation:
   - If `output: cv` → follow `resume_tailor.md`
   - If `output: lettre` → follow `cover_letter.md`
   - If `output: both` → run both workflows in sequence for consistency.
6. Use few-shot references from:
   - `examples/safran_cv_notes.md`
   - `examples/safran_letter_notes.md`
   - `CV_1page_Safran_AE_AIEngineer_Sami_Malek.pdf` and `lettre_Safran_AE_AIEngineer_Sami_Malek.pdf` (repository root)

## 3) Output Rules

### CV output (`output: cv` or `both`)
- Always produce a **1-page CV**.
- Keep HTML structure aligned with `sami_malek_master.html` style (clean ATS-friendly sections).
- Select only the most relevant:
  - **3-4 experiences**
  - **4-5 projects**
- Prioritize quantified impact where available.
- Keep role targeting explicit in summary, skills, and experience bullets.

### Cover letter output (`output: lettre` or `both`)
- 3-4 paragraphs.
- Target length: ~300 words.
- Respect requested language and tone.
- Must connect candidate evidence to job requirements from `cible`.

### Bilingual rule
- If `langue: both`, always output **FR and EN versions** (CV and/or letter depending on `output`).

## 4) Quality Checklist (must pass before final output)

- [ ] No fabricated experiences, projects, dates, or metrics.
- [ ] Uses available quantified achievements where relevant:
  - 55M MAD opportunity
  - 87% retention improvement
  - 98% accuracy
  - RMSE 0.298
- [ ] Integrates target-job keywords naturally from `cible`.
- [ ] CV remains ATS-friendly (standard sections, readable structure, no decorative complexity).
- [ ] Content is coherent with selected `type` template and `spécialités` mapping.
