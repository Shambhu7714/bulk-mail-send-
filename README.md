# Bulk Mail Sender

A small project for sending personalized voucher emails in bulk using an Excel file or manual entry.

Project structure

- `backend/` — Python backend (API endpoints to accept Excel uploads or manual requests and send emails).
- `frontend/` — Static frontend (HTML + JS) to upload Excel files, enter email template and trigger sending.

Features

- Send personalized emails by uploading an Excel with columns `Executive Name`, `Email`, `Voucher Amount`.
- Manual mode for sending to a comma-separated list of emails with a single name/amount.
- Simple logging output in the UI.
- A sample Excel download button in the frontend (creates a CSV/XLSX-styled template).

Quick start (Windows, PowerShell)

1. Backend (Python)

- Create and activate a virtual environment (if not already):

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- Install dependencies (if a `requirements.txt` exists):

```powershell
pip install -r requirements.txt
```

- Start the backend API (adjust the command to your app's entrypoint):

```powershell
# Example using uvicorn for a FastAPI app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Frontend (static)

- Serve files from `frontend/` (open `frontend/index.html` directly in the browser or use a simple static server):

```powershell
# From workspace root, using Python's HTTP server
cd frontend
python -m http.server 5500
# Then open http://localhost:5500 in your browser
```

3. Using the app

- In the UI enter your email template (use `<<Name>>` and `<<Amount>>` placeholders).
- Use the Excel upload area to choose an Excel file or use manual entry.
- Click the send button to invoke the backend endpoint. Responses and logs appear in the UI's logs area.

Important notes about Git and repository layout

- This workspace currently contains two Git repositories:
  - The root `email_send` repository (remote: `https://github.com/Shambhu7714/bulk-mail-send-.git`).
  - A nested `backend` repository at `backend/` (this is an independent repo inside the root repo).

- Because `backend` is a separate repository (it has its own `.git`), committing and pushing from the root repo does NOT automatically include the internal `backend` repository's commits or untracked files. If you want the `backend` code to be part of the root repository, you must remove the nested `.git` inside `backend` (this will make `backend` tracked by the root repo) or adopt a submodule/subtree approach.

Common Git actions

- Push root repo to GitHub (already set):

```powershell
Set-Location 'C:\Users\Shambhu\Desktop\email_send'
# push current branch (e.g. dev)
git push -u origin dev
```

- Commit & push inside `backend` (if you want `backend` repo contents on its remote):

```powershell
Set-Location 'C:\Users\Shambhu\Desktop\email_send\backend'
# stage and commit files
git add .
git commit -m "Add backend source files"
# push dev
git push -u origin dev
```

- Convert `backend` into part of the root repository (if desired):

```powershell
# WARNING: this removes the nested repo metadata. Backup if needed.
Remove-Item -LiteralPath 'C:\Users\Shambhu\Desktop\email_send\backend\.git' -Recurse -Force
Set-Location 'C:\Users\Shambhu\Desktop\email_send'
git add backend
git commit -m "Add backend files into root repo"
git push -u origin dev
```

Security & credentials

- For GitHub pushes over HTTPS you will need a GitHub Personal Access Token (PAT) instead of your password. Create one at https://github.com/settings/tokens with `repo` scope and use it as the password when prompted.
- For sending emails, keep SMTP credentials or API keys out of source control. Use environment variables or a `.env` file (and add it to `.gitignore`).

Next recommended steps

- Commit any remaining changes in `backend` and push from that repository (or tell me if you want me to remove the nested `.git` and add `backend` to the root repo).
- If you want, I can add a small `README` section with API endpoint docs if you point me to the backend code (e.g. `main.py` or `app.py`).

If you'd like any edits to this README (formatting, more details, API docs, or deployment instructions), tell me what to add and I'll update it.