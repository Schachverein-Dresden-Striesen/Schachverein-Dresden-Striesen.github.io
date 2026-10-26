# Agent skills

## Issue tracker

GitHub Issues are used for this repo. See [`docs/agents/issue-tracker.md`](docs/agents/issue-tracker.md).

### Triage labels

Default triage labels are used: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See [`docs/agents/triage-labels.md`](docs/agents/triage-labels.md).

## Domain docs

Single-context layout: root `CONTEXT.md` and `docs/adr/` are the reference docs for domain language and decisions. See [`docs/agents/domain.md`](docs/agents/domain.md).

## Repository context

Markdown- und Jekyll-Repository für die Website des Schachvereins Dresden-Striesen.

## Main role: editor

Improve clarity, flow, and impact without changing the author’s voice. Correct grammar, spelling, and structure; ask precise questions when facts are unclear.

## Quality and style standards

See [Developer Guide](DEVELOPER.md#qualitätsstandards) for Quality Rules and Style Rules that apply to all contributions, including Agent work.

## Repository skill seam

This seam selects the default. Mandatory checks for every contribution, including agent work, are the [Quality Rules and Style Rules](DEVELOPER.md#qualitätsstandards). `.agents/skills/` stays a broad optional toolkit; leave individual skills in place, including examples written for other stacks.

- **Website changes:** content, front matter, layout, Liquid includes, navigation, configuration, assets, and other published-site changes default to the documented Jekyll build and rendered-site inspection in [DEVELOPER.md](DEVELOPER.md). A new test framework or mocks are not required for these changes.
- **Testable application behavior:** application tests, TDD, and mocks are available when the change introduces behavior and seams that justify them.
- **Prototyping and debugging:** use framework-specific prototyping and advanced debugging only when the task needs them and the infrastructure exists. A static page or layout prototype does not assume a JavaScript framework. Scale diagnosis to the failure and the tools on hand; service instrumentation, fuzzing, or browser automation are not the default for a simple site issue.
- **Research:** choose delegation and a persistent Markdown report from the requested scope and deliverable. Answer a bounded question directly. When substantial documented research is requested, keep the research thorough and write the reusable report.
- **Glossary:** update [`GLOSSARY.md`](GLOSSARY.md) only when a domain term is clarified or changed. Ordinary unrelated work leaves the glossary unchanged.
