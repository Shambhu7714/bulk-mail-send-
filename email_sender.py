from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY, SENDER_EMAIL


# ---------------------------------------------------------
#  Replace placeholders with dynamic values
# ---------------------------------------------------------
def build_dynamic_message(template: str, name: str, amount: str) -> str:
    """
    Replaces placeholders in the HTML template:
       <<Name>>
       <<Amount>>
    """
    return (
        template.replace("<<Name>>", str(name))
                .replace("<<Amount>>", str(amount))
    )


# ---------------------------------------------------------
#  Send a dynamic HTML email using SendGrid
# ---------------------------------------------------------
def send_email_dynamic(receiver: str, subject: str, html_content: str) -> str:
    """
    Sends HTML email to a single receiver.
    Returns: "sent", "failed (code)", or "error: ..."
    """

    try:
        message = Mail(
            from_email=SENDER_EMAIL,
            to_emails=receiver,
            subject=subject,
            html_content=html_content
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        status_code = response.status_code

        # Logging
        if 200 <= status_code < 300:
            print(f"[SENT] {receiver}  Status={status_code}")
            return "sent"
        else:
            print(f"[FAILED] {receiver}  Status={status_code}")
            return f"failed ({status_code})"

    except Exception as e:
        print(f"[ERROR] {receiver}  Error={str(e)}")
        return f"error: {str(e)}"
