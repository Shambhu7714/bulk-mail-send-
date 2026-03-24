import uuid
from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks
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


# --- In-memory Task Tracking ---
tasks = {}

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

def run_email_task(task_id: str, data: list, subject: str, template: str, sender: str = None):
    total = len(data)
    tasks[task_id]["total"] = total
    
    for index, item in enumerate(data):
        name = item["name"]
        email = item["email"]
        amount = item["amount"]
        
        body = build_dynamic_message(template, name, amount)
        print(f"[{task_id}] [{index+1}/{total}] Sending to {email} | {name} | ₹{amount}")
        
        status = send_email_dynamic(email, subject, body, sender=sender)
        
        tasks[task_id]["logs"].append({
            "index": index + 1,
            "email": email,
            "name": str(name),
            "amount": str(amount),
            "status": status
        })
        tasks[task_id]["current"] = index + 1

    tasks[task_id]["status"] = "completed"
    print(f"[{task_id}] Bulk Send Completed")


@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    if task_id not in tasks:
        return {"error": "Task not found"}
    return tasks[task_id]


# ---------------------- Excel Upload ----------------------
@app.post("/send-excel-mails")
async def send_excel_mails(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    subject: str = Form(...),
    template: str = Form(...),
    sender: str = Form(None)
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

    total = len(df)
    data_to_send = []
    for index, row in df.iterrows():
        data_to_send.append({
            "name": row["Executive Name"],
            "email": str(row["Email"]).strip(),
            "amount": row["Voucher Amount"]
        })

    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "status": "processing",
        "current": 0,
        "total": total,
        "logs": [],
        "message": "Excel bulk send started"
    }

    background_tasks.add_task(run_email_task, task_id, data_to_send, subject, template, sender)

    return {"message": "Excel bulk send started in background", "task_id": task_id}



# ---------------------- Manual Sending ----------------------
@app.post("/send-manual-mails")
async def send_manual_mails(
    background_tasks: BackgroundTasks,
    emails: str = Form(...),
    subject: str = Form(...),
    template: str = Form(...),
    name: str = Form(...),
    amount: str = Form(...),
    sender: str = Form(None)
):

    email_list = [e.strip() for e in emails.split(",") if e.strip()]

    total = len(email_list)
    data_to_send = []
    for email in email_list:
        data_to_send.append({
            "name": name,
            "email": email,
            "amount": amount
        })

    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "status": "processing",
        "current": 0,
        "total": total,
        "logs": [],
        "message": "Manual bulk send started"
    }

    background_tasks.add_task(run_email_task, task_id, data_to_send, subject, template, sender)

    return {"message": "Manual bulk send started in background", "task_id": task_id}



# ---------------------- START SERVER ----------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

