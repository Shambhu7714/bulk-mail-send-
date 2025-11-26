Below is a **clean, professional, production-ready `README.md`** written **exactly for your current project structure**:

```
EMAIL_SEND/
│── backend/
│    ├── main.py
│    ├── email_sender.py
│    ├── config.py
│    ├── index.html
│    ├── requirements.txt
│    ├── Dockerfile
│    ├── .env
│    ├── .gitignore
│    └── venv/  (ignored)
```

The README includes:

✔ Installation
✔ Environment setup
✔ Running backend
✔ Accessing frontend
✔ Using Excel upload
✔ Manual email sending
✔ Docker instructions
✔ API reference
✔ Production deployment notes

---

# ⭐ **FINAL README.md**

Copy–paste into your `backend/README.md`

---

# 📧 Bulk Email Sender – Excel & Manual (FastAPI + SendGrid)

This project is a **full-featured bulk email sender** that allows sending personalized emails to recipients using:

* **Excel Upload**
* **Manual Email Entry**

The frontend UI is contained inside a **single `index.html` file** and is served directly by FastAPI.

The backend handles:

* Dynamic template placeholders (`<<Name>>`, `<<Amount>>`)
* SendGrid email delivery
* Excel parsing
* Clean JSON response logs

---

## 📁 Project Structure

```
backend/
│── main.py               # FastAPI backend + UI serving
│── email_sender.py       # SendGrid email sending module
│── config.py             # API keys & configuration
│── index.html            # Single-file frontend (HTML+CSS+JS)
│── requirements.txt      # Dependencies
│── Dockerfile            # Docker image for deployment
│── .env                  # Environment variables (NOT committed)
│── .gitignore
│── venv/                 # Virtual environment (ignored)
```

---

## 🚀 Features

### ✔ Single-file UI (`index.html`)

Contains all HTML + CSS + JavaScript for:

* Email template editor
* Excel upload
* Manual email sending
* Logs output section

### ✔ Dynamic Template Rendering

Supports placeholders:

* `<<Name>>`
* `<<Amount>>`

### ✔ Send Email Using Excel

Excel must contain:

* **Executive Name**
* **Email**
* **Voucher Amount**

### ✔ Manual Email Sending

User enters:

* Recipients (comma-separated)
* Name
* Amount
* Subject
* Template

### ✔ Logs Returned to UI

Shows:

* Sent emails
* Failed emails
* Debug info

---

## 🛠 Installation & Setup

### 1. Clone the project

```
git clone <your-repo>
cd EMAIL_SEND/backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create `.env` file

Inside `backend/.env`:

```
SENDGRID_API_KEY=YOUR_SENDGRID_KEY_HERE
SENDER_EMAIL=bajaj.finservhealth@almonds.ai
```

---

## ▶️ Running the Server

Run:

```
python main.py
```

You should see:

```
Uvicorn running on http://0.0.0.0:8000
```

---

## 🌐 Access the UI

Open in browser:

```
http://localhost:8000
```

This automatically loads the **index.html** UI from FastAPI.

---

## 🧪 API Endpoints

### **POST /send-excel-mails**

Send personalized emails using Excel.

Form fields:

* file (Excel)
* subject
* template (HTML template)

### **POST /send-manual-mails**

Send personalized emails manually.

Form fields:

* emails
* name
* amount
* subject
* template

---

## 📦 Running with Docker

### 1. Build Docker image

```
docker build -t bulk-mailer .
```

### 2. Run container

```
docker run -p 8000:8000 --env-file .env bulk-mailer
```

### 3. Open browser

```
http://localhost:8000
```

---

## 📬 Excel Requirements

Your Excel file **must** have the following columns:

| Executive Name | Email                                         | Voucher Amount |
| -------------- | --------------------------------------------- | -------------- |
| Rahul Sharma   | [email@example.com](mailto:email@example.com) | 1000           |
| Ankit Singh    | [test@gmail.com](mailto:test@gmail.com)       | 500            |

---

## 🎨 Template Placeholders

Your email template can include:

```
<<Name>>
<<Amount>>
```

FastAPI will replace them dynamically.

Example:

```html
<p>Dear <<Name>>,</p>
<p>You have won ₹<<Amount>> Amazon voucher!</p>
```

---

## 📝 Logs

Each request returns:

* email
* name
* amount
* status (“sent”, “failed”, “error”)

Example:

```json
{
  "message": "Emails sent successfully",
  "logs": [
    {
      "email": "test@gmail.com",
      "name": "Rahul",
      "amount": "1000",
      "status": "sent"
    }
  ]
}
```

---

## 🛡 Production Deployment Notes

For production, use:

* Docker
* NGINX reverse proxy
* Uvicorn workers (`--workers 4`)
* HTTPS (Let's Encrypt)

I can generate a full production setup if you need it.

---

## ❤️ Support or Improvements?

Tell me if you want:

* 🔧 CSV support
* 🔐 Admin login system
* 🎨 Branded HTML template
* 📊 Dashboard to track sent emails
* 📨 Attachments support
* 🚀 Auto-retry & queue system

---

# ✅ Project is now fully documented and deployment-ready 🚀

If you want the **production NGINX server setup**, just say:

👉 **“Create production deployment guide”**
