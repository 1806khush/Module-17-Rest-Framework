# otp_sender/utils.py
from twilio.rest import Client
from django.conf import settings
import random

def send_otp(phone_number):
    """Generate and send OTP to the user's phone using Twilio."""
    otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
    
    # Initialize Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    message = client.messages.create(
        body=f"Your OTP is {otp}. Please use this to complete your registration.",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    
    if message.sid:
        return otp  # Return OTP to store for verification
    else:
        return None
