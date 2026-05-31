# Job Applications Skill System

This repository is Sami MALEK's personal job-application workspace powered by GitHub Copilot. It centralizes the master CV sources, specialty mappings, writing templates, and generated outputs used to tailor cover letters and related application material in French and English.

## Purpose

Use this repository to:
- tailor motivation letters / cover letters for internships, alternance roles, jobs, and academic programs;
- keep a stable master CV source in English and French;
- route each application toward the most relevant experiences and projects;
- generate reusable outputs in a consistent format.

## Repository Layout

- `/SKILL.md` — entry point for the Copilot letter-writing workflow
- `/master_cv/` — mirrored HTML master CV sources used as the canonical reference during tailoring
- `/specialty_mapping.md` — which experiences/projects to prioritize by specialty
- `/templates/` — structured guides for each application type and language
- `/examples/README.md` — notes on the example PDFs kept at the repository root
- `/output/` — generated deliverables

## Prompt Schema

Use the following prompt with Copilot:

```text
@lettre
type: stage | alternance | poste | formation
langue: fr | en
spécialités: [comma-separated from: AI/LLM/RAG, data_science, mlops, computer_vision, big_data, nlp, full_stack]
cible: [URL or pasted description]
ton: (optional) formel | enthousiaste | sobre
notes: (optional) free text
```

## Recommended Workflow

1. Paste the `@lettre` block.
2. Set the application `type` and `langue`.
3. Choose the 1-3 `spécialités` that best match the target.
4. Add the target URL or paste the opportunity description in `cible`.
5. Optionally refine tone and extra notes.
6. Let Copilot:
   - read `/specialty_mapping.md` to select the strongest proof points;
   - open the matching template in `/templates/`;
   - draft the full letter;
   - add a short strategic note explaining the positioning choices.

## Output Expectation

Each generated output should contain:
- a complete ready-to-send letter;
- a short strategic note (3-5 bullets) explaining what was emphasized, why, and what can still be personalized.

## Source Material

The original root-level files remain untouched on purpose:
- `sami_malek_master.html`
- `sami_malek_master_fr.html`
- `sami_malek_master_fr.pdf`
- example tailored CV and cover letter PDFs
- legacy skill notes (`resume_tailor.md`, `cover_letter.md`)

This setup lets Copilot use the new structured system without losing the original source assets.
