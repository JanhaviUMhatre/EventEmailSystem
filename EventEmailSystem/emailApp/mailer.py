from django.conf import settings

def send_mail(plain_message, recipient_list, subject):
    try:
        send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient_list]
            )
    except Exception as e:
        print("Error in sending mail")
        return