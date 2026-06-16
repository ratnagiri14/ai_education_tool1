# ai_education_tool1

AI Autism Support Toolkit built with Streamlit and OpenAI.

## Files

- `app.py`: simple UI version
- `main_app.py`: styled app UI
- `main_app1.py`: full AI-powered toolkit
- `requirements.txt`: dependencies

## Setup & Secrets

Store your OpenAI key securely — do NOT commit it to git.

- Use Streamlit Cloud secrets (recommended) or create a local file at `.streamlit/secrets.toml` with this content:

```
OPENAI_API_KEY = "REPLACE_WITH_YOUR_KEY"
# Optional: OPENAI_MODEL = "gpt-4o-mini"
```

- After adding the key, run the app:

```bash
streamlit run streamlit_app.py
```

If the app reports a model error, set `OPENAI_MODEL` in secrets to a model your API key can access.
