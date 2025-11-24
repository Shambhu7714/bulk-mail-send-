git commit -m "Add backend files into root repo"
# Bulk Mail Sender

A small project for sending personalized voucher emails in bulk using an Excel file or manual entry.

Current repository layout (consolidated)

- `main.py` — Optional single-file server (at repository root). When run this serves the frontend and exposes the same API endpoints; useful for easy single-file deployment.
- `backend/` — Primary backend folder. It now contains `index.html` (the full frontend inlined), backend Python code (`main.py`, `email_sender.py`, `config.py`), and `requirements.txt`.

What changed

- The frontend was consolidated into the backend: `backend/index.html` is a single-file frontend with CSS and JS inlined.
- The previous `frontend/` files have been removed and the repository includes the consolidated version under `backend/`.
- A branch named `mail-send` was created that contains this consolidation (you can find it on the remote).

Files of interest

- `main.py` — (optional) a single runnable FastAPI app that serves `backend/index.html` and implements the `/send-excel-mails` and `/send-manual-mails` endpoints. Use this if you want a single-file deployment.
- `backend/main.py` — original FastAPI app (if you prefer running the backend and serving static files with another server).
- `backend/index.html` — the inlined frontend (open directly or served by the backend).
- `backend/email_sender.py` — SendGrid integration for sending emails.
- `backend/config.py` — environment-based settings (SENDGRID_API_KEY, SENDER_EMAIL).
- `backend/requirements.txt` — Python dependencies.

Quick start — single-file server (recommended for easiest deployment)

1. Create and activate a Python virtual environment (PowerShell):

```powershell
cd C:\Users\Shambhu\Desktop\email_send
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r backend\requirements.txt
```

3. (Optional) Configure environment variables — create a `.env` in the repository root or set variables in your environment:

```
SENDGRID_API_KEY=your_sendgrid_api_key
SENDER_EMAIL=you@yourdomain.com
```

4. Run the single-file server:

```powershell
python single_app.py
# Open http://localhost:8000 in the browser
```

Notes: when running `single_app.py` the frontend is served at `/` and API endpoints are on the same origin (`/send-excel-mails`, `/send-manual-mails`). This avoids CORS and makes deployment as a single process easier.

Alternative — run the backend only and open static frontend separately

- Serve `backend/index.html` with a static server and run `backend/main.py` with `uvicorn main:app` if you prefer separating processes.

Git notes

- The repository remote was set to `https://github.com/Shambhu7714/bulk-mail-send-.git` previously.
- A branch `mail-send` was created that contains the consolidated frontend. You can create a pull request from that branch if you want to merge these changes.
- I have left commits local or pushed only to branches you requested; confirm before doing any additional pushes to PR/merge.

Security & credentials

- For GitHub pushes over HTTPS use a Personal Access Token (PAT) when prompted for a password.
- Keep SendGrid API keys and sender email out of source control (use `.env` and add `.env` to `.gitignore`).

Next steps (suggested)

- Run the app locally with `python single_app.py` and test the UI and email sending (use test SendGrid/API keys or stub out `send_email_dynamic` for dry runs).
- If you'd like, I can remove the old backend-only files or fully convert the repo to the single-file layout (delete backups). Tell me whether to commit and push the consolidation branch (`mail-send`) or wait.

If you'd like more details in the README (example Excel file, API response format, or deployment instructions for a cloud provider), tell me which and I'll add it.
