# Contributing

Research Paper Orchestra is publicly readable but **proprietary**. Permission to view this repository does not grant permission to redistribute or reuse original code. Contact the copyright holder before submitting material that needs redistribution or before creating derivative releases.

## Development standards

1. Start from a defined research use case and the corresponding role guide.
2. Preserve source provenance, evidence labels, reviewer severity classes and implementation-limit disclosures.
3. Keep reusable role knowledge in `skills/research-paper-orchestra/references/`.
4. Validate locally: `python3 scripts/validate_plugin.py` and `python3 -m unittest discover -s tests -v`.
5. Use meaningful conventional commits. Do not introduce automatic workflows, deployment hooks or paid API calls without explicit owner approval.

Do not commit real patient data, private manuscripts, API credentials or copyrighted venue templates without permission.
