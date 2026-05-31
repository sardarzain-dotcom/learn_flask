# learn_flask

Lightweight writing-style tools for reducing AI-sounding phrasing and improving clarity.

## Files

- `ai_style_filter.py`: CLI tool to analyze and optionally rewrite text.
- `anti-ai-writing-style.md`: Style guidelines and usage notes.
- `chatgpt-ready-style.md`: Prompt-friendly condensed instructions.
- `Dockerfile`: Containerized way to run the CLI.

## Local usage

```bash
python3 ai_style_filter.py your-draft.md
python3 ai_style_filter.py your-draft.md --profile academic
python3 ai_style_filter.py your-draft.md --profile scientific --output cleaned.md
python3 ai_style_filter.py your-draft.md --profile resume-ats --write
```

## Docker usage

Build the image:

```bash
docker build -t ai-style-filter .
```

Run analysis:

```bash
docker run --rm -v "$PWD:/work" ai-style-filter /work/your-draft.md
```

Run with profile and write output to a new file:

```bash
docker run --rm -v "$PWD:/work" ai-style-filter /work/your-draft.md --profile scientific --output /work/cleaned.md
```

Overwrite the input file in place:

```bash
docker run --rm -v "$PWD:/work" ai-style-filter /work/your-draft.md --profile resume-ats --write
```