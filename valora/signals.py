# from django.utils.translation import ugettext_lazy as _
# from django.dispatch import Signal, receiver
# from django.core.mail import EmailMessage
# import traceback
# from django.template.loader import render_to_string
# from datetime import date
# from decimal import Decimal
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.utils import formats

# signal_server_error = Signal(providing_args=["instance"])


# @receiver(signal_server_error)
# def mail_server_error(sender, request, **kwargs):
#     if settings.DEBUG:  # DO NOTHING
#         return True
    
#     from_email = ''
#     recipient_list = ['']
#     subject = _("")
#     context = {
#         'date': formats.date_format(date.today(), "SHORT_DATE_FORMAT"),
#         '': ,
#         '': ,
#     }
#     template = render_to_string("notify/server_error.html", context)
    
#     email = EmailMessage(
#         from_email=from_email,
#         to=recipient_list,
#         subject=subject,
#         headers=context,
#         body=template
#     )
#     email.content_subtype = "html"

#     try:
#         email.send()
#     except Exception as e:
#         print(e)
#         traceback.print_exc()