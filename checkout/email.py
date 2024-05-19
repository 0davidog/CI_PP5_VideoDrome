from django.conf import settings

def send_confirmation_email(self, order):

    """Send the user a confirmation email"""

    customer_email = order.email

    from django.core.mail import EmailMessage

    email_subject = f'{order.number}'
    email_body = 'Here is the message.'
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [customer_email]

    email = EmailMessage(email_subject, email_body, sender_email, recipient_list)
    email.content_subtype = "html"  # Set the content type to HTML
    email.send()