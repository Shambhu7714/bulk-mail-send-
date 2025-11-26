import uvicorn
import pandas as pd
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from email_sender import send_email_dynamic, build_dynamic_message

app = FastAPI(title="Bulk Mailer", version="2.1")

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🔥 Fix for Excel hidden spaces, tabs, unicode
def normalize(col: str):
    if not isinstance(col, str):
        col = str(col)

    return (
        col.replace("\u00A0", " ")  # non-breaking space
           .replace("\t", " ")     # tabs
           .replace("\r", "")
           .replace("\n", "")
           .strip()                # remove leading/trailing spaces
    )


@app.get("/")
def home():
    return FileResponse("index.html")


# ---------------------- Excel Upload ----------------------
@app.post("/send-excel-mails")
async def send_excel_mails(
    file: UploadFile = File(...),
    subject: str = Form(...),
    template: str = Form(...)
):
    try:
        df = pd.read_excel(file.file)
    except Exception as e:
        return {"error": f"Could not read Excel file: {str(e)}"}

    # Normalize columns
    df.columns = [normalize(c) for c in df.columns]

    # Print detected columns (debug)
    print("🔍 Excel Columns Detected:", df.columns.tolist())

    required = ["Executive Name", "Email", "Voucher Amount"]

    # Validate
    missing = [r for r in required if r not in df.columns]
    if missing:
        return {
            "error": f"Missing columns: {missing}. Detected columns: {df.columns.tolist()}"
        }

    logs = []
    total = len(df)

    print(f"\n=== Excel Bulk Send Started ({total} rows) ===")

    for index, row in df.iterrows():
        name = row["Executive Name"]
        email = str(row["Email"]).strip()
        amount = row["Voucher Amount"]

        body = build_dynamic_message(template, name, amount)

        print(f"[{index+1}/{total}] Sending to {email} | {name} | ₹{amount}")

        status = send_email_dynamic(email, subject, body)

        logs.append({
            "row": index + 1,
            "email": email,
            "name": str(name),
            "amount": str(amount),
            "status": status
        })

    print("=== Excel Bulk Send Completed ===\n")

    return {"message": "Excel emails sent successfully!", "logs": logs}



# ---------------------- Manual Sending ----------------------
@app.post("/send-manual-mails")
async def send_manual_mails(
    emails: str = Form(...),
    subject: str = Form(...),
    template: str = Form(...),
    name: str = Form(...),
    amount: str = Form(...)
):

    email_list = [e.strip() for e in emails.split(",") if e.strip()]

    logs = []
    total = len(email_list)

    print(f"\n=== Manual Bulk Send Started ({total} emails) ===")

    for index, email in enumerate(email_list, start=1):
        body = build_dynamic_message(template, name, amount)

        print(f"[{index}/{total}] Sending to {email} | {name} | ₹{amount}")

        status = send_email_dynamic(email, subject, body)

        logs.append({
            "index": index,
            "email": email,
            "name": name,
            "amount": amount,
            "status": status
        })

    print("=== Manual Bulk Send Completed ===\n")

    return {"message": "Manual emails sent successfully!", "logs": logs}



# ---------------------- START SERVER ----------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
