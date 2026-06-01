# SKILL — Job Application Automation (Sami MALEK)

## Command Interface

```yaml
type: stage | alternance | poste | formation
langue: fr | en
spécialités: [list from specialty_mapping.json]
cible: <job posting URL or full text>
ton: formel | enthousiaste | sobre        # optional, default: sobre
notes: <specific constraints or emphasis> # optional
```

## Execution Flow

### 1) Analyze target (`cible`)
Extract and rank:
- hard skills
- domain keywords
- experience level signals
- business/context signals
- company tone cues

### 2) Load specialty evidence
Open `specialty_mapping.json` and pull matching:
- experiences
- projects
- skills
- quantified achievements
- cover-letter achievement anchors

### 3) Generate tailored resume
Use `templates/resume_tailoring_system.md` rules:
- Dynamic summary aligned with role priorities
- Reordered bullets (most relevant first)
- Natural keyword incorporation for ATS
- Clean formatting (no tables, no graphics, no columns required by ATS parser)
- Language adaptation (`fr`/`en`)
- Length rule: 1 page for early-career, up to 2 pages for senior role targets

### 4) Generate tailored cover letter
Use `templates/cover_letter_system.md` rules:
- 3-4 paragraph narrative
- 2-3 concrete achievements mapped to target needs
- Natural human tone (non-robotic)
- Optional hiring manager personalization when available
- Language adaptation (`fr`/`en`)

### 5) Validate before output
- No fabricated claims
- Metrics are verifiable from source materials
- Industry terminology is accurate
- Resume is ATS-safe
- Cover letter closes with target-specific motivation

## Output Contract

- Resume: `outputs/CV_{type}_{langue}_{target_slug}_Sami_Malek.(md|html|pdf)`
- Cover letter: `outputs/lettre_{type}_{langue}_{target_slug}_Sami_Malek.(md|pdf)`

## Source of Truth

- Master CVs: `sami_malek_master.html`, `sami_malek_master_fr.html`
- Tailoring guides: `resume_tailor.md`, `cover_letter.md`
- Specialty map: `specialty_mapping.json`
- Real references: Safran example outputs in repository root
