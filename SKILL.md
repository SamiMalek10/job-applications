# Job Application System — Sami MALEK

One command → tailored 1-page CV + cover letter, in French or English.

---

## Quick Command

```
@cv-lettre
type: stage | alternance | poste | formation
langue: fr | en
spécialités: [tags from list below, comma-separated]
cible: [paste full job description OR URL]
ton: formel | enthousiaste | sobre        (default: enthousiaste)
output: cv | lettre | both               (default: both)
notes: [optional — "mentioned by X", "emphasize governance", etc.]
```

**Example:**
```
@cv-lettre
type: stage
langue: fr
spécialités: AI/LLM/RAG, mlops
cible: [job description pasted here]
ton: enthousiaste
notes: insister sur GovernHQ et l'expérience GETEAM
```

---

## Specialty Tags

| Tag | What it covers |
|-----|----------------|
| `AI/LLM/RAG` | LLM gateway (GETEAM), multi-agent RAG 87% retention (3D Smart Factory), AI governance GovernHQ (PM Accelerator) |
| `data_science` | Customer segmentation 55M MAD (Laprophan), Power BI, predictive regression, K-Means |
| `computer_vision` | Meningioma 98% accuracy (ResNet/VGG ensemble), YOLOv8 fruit detection, ViT banking docs |
| `big_data` | PySpark/HDFS football market value (RMSE 0.298), Hadoop/Hive log pipeline, Spark Streaming + Kafka |
| `mlops` | MLflow experiment tracking, Docker/Docker Compose, JupyterHub private cloud, containerized deployments |
| `nlp` | Whisper+NLLB judicial transcription (Ministry of Justice), Hugging Face fine-tuning, AvicennAi medical chatbot |
| `full_stack` | FastAPI microservices, Flask/React.js judicial platform, Streamlit dashboards, Spring Boot MVC |
| `iot` | ESP32 PIR motion detection, Wokwi/Tinkercad simulation, C/C++ firmware |

---

## How This System Works

### Step 1 — Analyze the job description (`cible`)
Extract: required skills · nice-to-have · keywords · company culture signals · role pain point

### Step 2 — Load specialty mapping
Open `specialty_mapping.md` → find the matching tags → get the ranked list of experiences, projects, skills, and cover letter hooks.

### Step 3 — Build the 1-page CV (if `output: cv` or `both`)
1. Load `cv/content_blocks.md` (pre-structured, 1-page-ready content)
2. Select: top 2–3 experiences + 3–4 projects + relevant skills
3. Write tailored professional summary (3–4 lines, mirror job description keywords)
4. Format as clean HTML using the master resume as style reference
5. Save as: `outputs/CV_1page_{Company}_{Role}_{Lang}_Sami_Malek.html`

### Step 4 — Write the cover letter (if `output: lettre` or `both`)
1. Load the appropriate template: `templates/cover_letter_fr.md` or `templates/cover_letter_en.md`
2. Pick the 2–3 strongest achievement hooks from `specialty_mapping.md`
3. Write opening that does NOT start with "I" — lead with value or insight
4. Body: strongest alignment → unique differentiator → company-specific signal
5. Save as: `outputs/lettre_{Company}_{Role}_{Lang}_Sami_Malek.md`

---

## File Map

| File | Purpose |
|------|---------|
| `SKILL.md` | **This file** — command interface + workflow |
| `specialty_mapping.md` | Domain → experiences/projects/skills/hooks lookup table |
| `cv/content_blocks.md` | Pre-extracted structured content for fast 1-page CV assembly |
| `templates/cover_letter_fr.md` | French letter template with placeholders |
| `templates/cover_letter_en.md` | English letter template with placeholders |
| `resume_tailor.md` | Claude skill: detailed CV tailoring instructions |
| `cover_letter.md` | Claude skill: detailed cover letter instructions |
| `sami_malek_master.html` | Full English resume — source of truth |
| `sami_malek_master_fr.html` | Full French resume — source of truth |
| `examples/` | Real application examples (Safran) for few-shot reference |

---

## Output Naming Convention

```
outputs/CV_1page_{Company}_{Role}_{Lang}_Sami_Malek.html
outputs/lettre_{Company}_{Role}_{Lang}_Sami_Malek.md
```

Examples:
- `outputs/CV_1page_Safran_AIEngineer_EN_Sami_Malek.html`
- `outputs/lettre_Dassault_IngDonneesIA_FR_Sami_Malek.md`

---

## Quality Checklist (auto-verify before output)

**CV:**
- [ ] 1 page only (for <10 years experience)
- [ ] Professional summary mirrors 3+ keywords from job description
- [ ] Every bullet: Action verb + What + How/Result (quantified where possible)
- [ ] Skills section lists only skills substantiated by experience
- [ ] No personal pronouns (I/me/my)

**Cover Letter:**
- [ ] Does NOT start with "I" or "Je"
- [ ] ≤ 4 paragraphs, ≤ 400 words
- [ ] At least 2 specific metrics or achievements cited
- [ ] Company-specific signal in closing paragraph
- [ ] Tone matches `ton` parameter
