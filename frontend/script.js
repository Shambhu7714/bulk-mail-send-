const API_BASE = "http://localhost:8000";

function getTemplate() {
  return document.getElementById("templateBox").value;
}

async function sendExcel() {
  const fileInput = document.getElementById("excelFile");
  const subject = document.getElementById("excelSubject").value.trim();
  const template = getTemplate();
  const output = document.getElementById("output");

  if (!fileInput.files[0]) {
    alert("Please select an Excel file.");
    return;
  }
  if (!subject) {
    alert("Please enter an email subject.");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  formData.append("subject", subject);
  formData.append("template", template);

  output.textContent = "Sending emails from Excel...\nPlease wait...";

  try {
    const res = await fetch(`${API_BASE}/send-excel-mails`, {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    output.textContent = "Error: " + err;
  }
}

async function sendManual() {
  const emails = document.getElementById("manualEmails").value.trim();
  const subject = document.getElementById("manualSubject").value.trim();
  const name = document.getElementById("manualName").value.trim();
  const amount = document.getElementById("manualAmount").value.trim();
  const template = getTemplate();
  const output = document.getElementById("output");

  if (!emails) {
    alert("Please enter at least one email address.");
    return;
  }
  if (!subject) {
    alert("Please enter an email subject.");
    return;
  }
  if (!name) {
    alert("Please enter a name.");
    return;
  }
  if (!amount) {
    alert("Please enter voucher amount.");
    return;
  }

  const formData = new FormData();
  formData.append("emails", emails);
  formData.append("subject", subject);
  formData.append("template", template);
  formData.append("name", name);
  formData.append("amount", amount);

  output.textContent = "Sending manual emails...\nPlease wait...";

  try {
    const res = await fetch(`${API_BASE}/send-manual-mails`, {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    output.textContent = "Error: " + err;
  }
}
