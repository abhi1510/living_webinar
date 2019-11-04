from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = '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'
FROM_EMAIL = 'support@livingwebinar.com'


def send_email(subject, msg_html, to_emails):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_emails,
        subject=subject,
        html_content=msg_html
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        # log the above
    except:
        # log the error
        return False
    return True
