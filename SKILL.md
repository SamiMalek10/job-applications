# Job Application System — Sami MALEK

One command → tailored 1-page CV + cover letter, in French or English.

---

## Quick Command

Preferred invocation:

```text
@lettre
```

Supported alias:

```text
@cv-lettre
```

Syntax:

```yaml
@lettre
 type: stage | alternance | poste | formation
 langue: fr | en
 spécialités: AI/LLM/RAG, data_science, cloud, business_analytics, mlops, nlp, ...
 cible: pasted job description OR URL
 output: cv | lettre | both
 ton: formel | enthousiaste | sobre
 hiring_manager: optional
 notes: optional personal notes or signals to include
```

**Example — French training program**

```yaml
@lettre
 type: formation
 langue: fr
 spécialités: AI/LLM/RAG, mlops
 cible: Master 2 Informatique / Business Intelligence et Analytics
 output: both
 ton: formel
 notes: insister sur Laprophan, Power BI et l'articulation IA + BI
```

**Example — English internship**

```yaml
@lettre
 type: stage
 langue: en
 spécialités: data_science, cloud
 cible: https://company.example/jobs/data-analytics-intern
 output: cv
 ton: enthousiaste
 notes: highlight SAP analytics and dashboard delivery
```

---

## Specialty Tags

| Tag | What it covers |
|-----|----------------|
| `AI/LLM/RAG` | LLM gateway (GETEAM), multi-agent RAG 87% retention (3D Smart Factory), AI governance GovernHQ (PM Accelerator) |
| `data_science` | Customer segmentation 55M MAD (Laprophan), Power BI, predictive regression, K-Means |
| `business_analytics` | SAP analytics, Power BI/Tableau, business intelligence framing, demand forecasting |
| `cloud` | Dockerized ML systems, private cloud/JupyterHub, distributed data tooling, production observability |
| `computer_vision` | Meningioma 98% accuracy (ResNet/VGG ensemble), YOLOv8 fruit detection, ViT banking docs |
| `big_data` | PySpark/HDFS football market value (RMSE 0.298), Hadoop/Hive log pipeline, Spark Streaming + Kafka |
| `mlops` | MLflow experiment tracking, Docker/Docker Compose, JupyterHub private cloud, containerized deployments |
| `nlp` | Whisper+NLLB judicial transcription (Ministry of Justice), Hugging Face fine-tuning, AvicennAi medical chatbot |
| `full_stack` | FastAPI microservices, Flask/React.js judicial platform, Streamlit dashboards, Spring Boot MVC |
| `iot` | ESP32 PIR motion detection, Wokwi/Tinkercad simulation, C/C++ firmware |

---

## How This System Works

### Step 1 — Analyze the job description (`cible`)
Extract: required skills · nice-to-have · keywords · company/program signals · role pain point.

### Step 2 — Select the scenario templates
- Resume template: `templates/resume/{type}_{lang}.md`
- Cover letter template: `templates/cover_letter/{type}_{lang}.md`

### Step 3 — Load the reusable content source
Open `cv/content_blocks.md` and `specialty_mapping.md` to pull only verified facts, ranked experiences, projects, skills, and narrative hooks.

### Step 4 — Assemble the 1-page CV (if `output: cv` or `both`)
1. Match `spécialités` to ranked experience/project blocks.
2. Keep the CV to the strongest 2–3 experiences + 2–4 projects.
3. Mirror 3+ target keywords in the summary and skills section.
4. Format as clean ATS-friendly HTML using the master CV as style reference.
5. Save as `outputs/CV_1page_{Company}_{Role}_{Lang}_Sami_Malek.html`.

### Step 5 — Write the cover letter (if `output: lettre` or `both`)
1. Use the matching cover letter template.
2. Open with value, never with “Je” / “I”.
3. Use 2–3 quantified hooks from `specialty_mapping.md`.
4. Personalize the closing with company/program specifics and optional notes.
5. Save as `outputs/lettre_{Company}_{Role}_{Lang}_Sami_Malek.md`.

### Step 6 — Optional helper for path consistency
Use:

```bash
python3 scripts/application_helper.py --type formation --lang fr --company "Universite Lyon 2" --role "Master BI and Analytics"
```

This prints the expected template paths and normalized output filenames.

---

## File Map

| File | Purpose |
|------|---------|
| `SKILL.md` | Main command interface + workflow |
| `cv/content_blocks.md` | Reusable bilingual content blocks for 1-page CV assembly |
| `specialty_mapping.md` | Domain → experiences/projects/skills/hooks lookup table |
| `templates/resume/*.md` | Job-type × language CV templates |
| `templates/cover_letter/*.md` | Job-type × language cover letter templates |
| `resume_tailor.md` | Detailed CV tailoring instructions |
| `cover_letter.md` | Detailed cover letter instructions |
| `scripts/application_helper.py` | Output naming + template lookup helper |
| `examples/README.md` | Reference examples already present in the repository |
| `outputs/` | Destination for generated CVs and letters |
| `sami_malek_master.html` | Full English resume — source of truth |
| `sami_malek_master_fr.html` | Full French resume — source of truth |

---

## Output Naming Convention

```text
outputs/CV_1page_{Company}_{Role}_{Lang}_Sami_Malek.html
outputs/lettre_{Company}_{Role}_{Lang}_Sami_Malek.md
```

Examples:
- `outputs/CV_1page_Safran_AIEngineer_EN_Sami_Malek.html`
- `outputs/lettre_UniversiteLyon2_MasterBIA_FR_Sami_Malek.md`

---

## Quality Checklist (auto-verify before output)

**CV**
- [ ] 1 page only (for <10 years experience)
- [ ] Summary mirrors at least 3 keywords from the target posting
- [ ] Every bullet = action + scope + result
- [ ] Skills section lists only substantiated skills
- [ ] No fabricated tools, titles, metrics, or dates

**Cover Letter**
- [ ] Does not start with “I” or “Je”
- [ ] ≤ 4 paragraphs and ≤ 400 words
- [ ] Includes at least 2 specific achievements or metrics
- [ ] Closing mentions a concrete company/program signal
- [ ] Tone matches `ton` and language stays natural
