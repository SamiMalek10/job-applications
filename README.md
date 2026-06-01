# Job Application Automation System

Automated framework to generate tailored resumes and cover letters for Sami Malek, in French or English, from a target job/internship/training description.

## Inputs

```yaml
type: stage | alternance | poste | formation
language: fr | en                          # alias: langue
specialties: [ai_llm_rag, data_science, computer_vision, mlops, backend_web, big_data] # alias: spécialités
cible: <job posting URL or pasted description>
ton: formel | enthousiaste | sobre   # optional
notes: <specific angle to emphasize> # optional
```

## Outputs

- Tailored ATS-friendly resume (1 page for early-career profiles, 2 pages for senior roles)
- Tailored cover letter (3-4 paragraphs)
- Both in requested language (`fr` or `en`)

## Repository Layout

- `SKILL.md`: automation entry point and execution workflow
- `specialty_mapping.json`: reusable mapping from specialty to experiences/projects/skills
- `templates/resume_tailoring_system.md`: resume tailoring rules and checks
- `templates/cover_letter_system.md`: cover-letter generation rules and checks
- `templates/prompt_examples.md`: few-shot prompt patterns
- `examples/safran_resume_analysis.md`: analysis of Safran resume strategy
- `examples/safran_cover_letter_analysis.md`: analysis of Safran cover letter strategy

## Reference Materials

- `sami_malek_master.html`
- `sami_malek_master_fr.html`
- `cover_letter.md`
- `resume_tailor.md`
- `CV_1page_Safran_AE_AIEngineer_Sami_Malek.pdf`
- `lettre_Safran_AE_AIEngineer_Sami_Malek.pdf`

## Workflow Summary

1. Parse target posting and extract requirements/keywords.
2. Load matching specialties from `specialty_mapping.json`.
3. Build resume summary and reordered bullets around role fit.
4. Generate cover letter with 2-3 concrete achievements.
5. Run quality checks for ATS formatting, factual accuracy, and language/tone.
