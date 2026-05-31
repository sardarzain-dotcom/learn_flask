FROM python:3.12-slim

WORKDIR /app

# Copy the CLI script and docs used by the tool.
COPY ai_style_filter.py anti-ai-writing-style.md chatgpt-ready-style.md README.md ./

ENTRYPOINT ["python", "/app/ai_style_filter.py"]
CMD ["--help"]
