# Resume Tailoring System

## Goal
Generate an ATS-optimized resume tailored to a target posting while preserving factual accuracy.

## Inputs
- `type`: stage | alternance | poste | formation
- `langue`: fr | en
- `spécialités`: one or more specialties from `specialty_mapping.json`
- `cible`: job posting URL or full description text
- `ton`: optional
- `notes`: optional

## Generation Rules

1. **Requirement Extraction**
   - Extract top required skills, tools, and mission keywords.
   - Detect seniority and decide length:
     - Early-career profile/target: 1 page
     - Senior profile/target: up to 2 pages

2. **Experience Mapping**
   - Map each critical requirement to evidence from master CV and specialty mapping.
   - Prioritize experiences with quantified outcomes.

3. **Dynamic Summary**
   - 3-4 lines max.
   - Include 2-4 target keywords naturally.
   - Align wording to target domain and language.

4. **Bullet Reordering**
   - Reorder achievements by relevance to the target role.
   - Keep bullet structure: action + implementation + measurable outcome.

5. **ATS Constraints**
   - No tables, no icons, no graphics, no text in images.
   - Standard section names (Experience, Projects, Skills, Education).
   - Clean chronology and consistent dates.

6. **Bilingual Quality**
   - French output: native French phrasing (not literal translation).
   - English output: concise business/technical language.

## Validation Checklist
- Facts match source CV materials.
- Keyword usage is natural, not stuffed.
- Skills listed are supported by evidence.
- Formatting remains parser-friendly.
