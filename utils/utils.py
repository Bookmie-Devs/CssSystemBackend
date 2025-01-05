from django.template.loader import render_to_string
from django.conf import settings
from random import sample
from string import ascii_uppercase, ascii_lowercase, digits
import requests


def is_mobile(request):
    # check if user is trying to access the admin from mobile
    user_agent = request.META.get("HTTP_USER_AGENT", "").lower()

    mobile_keywords = [
        "iphone",
        "android",
        "mobile",
        "blackberry",
        "windows phone",
    ]

    if any(keyword in user_agent for keyword in mobile_keywords):
        return True
    else:
        return False


def generate_code(max=4, reset_password=False):
    codes = digits + ascii_lowercase + ascii_uppercase
    if reset_password:
        codes = digits
    code = sample(population=codes, k=max)
    return "".join(code)


def normalize_phone(number: str):
    valid_phone = number.replace(" ", "")
    if valid_phone.__len__() == 14:
        return valid_phone.removeprefix("+233")

    elif valid_phone.__len__() == 13:
        return ("0" + "%s") % valid_phone.removeprefix("+233")


def send_sms_message(phone, template, context):
    msg = render_to_string(template, context)
    endpoint = "https://apps.mnotify.net/smsapi/"
    params = {
        "key": settings.SMS_API_KEY,
        "to": phone,
        "msg": msg,
        "sender_id": settings.SENDER_ID,
    }
    requests.post(url=endpoint, params=params)