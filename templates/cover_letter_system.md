# Cover Letter System

## Goal
Generate a tailored 3-4 paragraph cover letter aligned with the target posting and company context.

## Inputs
- `type`: stage | alternance | poste | formation
- `langue`: fr | en
- `spécialités`: one or more specialties from `specialty_mapping.json`
- `cible`: target posting text or URL
- `ton`: formel | enthousiaste | sobre (optional)
- `notes`: optional personalization constraints

## Generation Rules

1. **Opening Paragraph**
   - Immediate relevance to target role/program.
   - Mention role/company/program name when available.
   - Optionally address hiring manager by name if provided.

2. **Body Paragraphs (2 paragraphs)**
   - Anchor 2-3 achievements directly tied to target requirements.
   - Prefer quantified outcomes (e.g., 55M MAD, +87%, 98%).
   - Demonstrate match between technical depth and expected impact.

3. **Closing Paragraph**
   - Explain motivation for this target specifically (team, mission, program fit).
   - End with a professional, natural call to action.

4. **Tone and Language**
   - Human tone, fluent transitions, no robotic sentence patterns.
   - French and English outputs must each read as native writing.

## Hard Constraints
- No fabrication of people, projects, metrics, or responsibilities.
- Max 4 paragraphs.
- Keep concise and scannable.
