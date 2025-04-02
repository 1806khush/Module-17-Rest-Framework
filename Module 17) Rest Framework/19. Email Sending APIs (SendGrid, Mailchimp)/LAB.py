# email_sender/utils.py
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from django.conf import settings

def send_confirmation_email(user_email):
    """Send confirmation email to the user after registration."""
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    from_email = Email(settings.SENDGRID_DEFAULT_FROM_EMAIL)
    to_email = To(user_email)
    subject = "Welcome to Our Service!"
    content = Content("text/plain", "Thank you for registering. Your account is now active.")
    
    mail = Mail(from_email, to_email, subject, content)
    
    try:
        response = sg.send(mail)
        if response.status_code == 202:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
# email_sender/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .utils import send_confirmation_email

def register(request):
    """Handle user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            
            # Send the confirmation email to the user
            user_email = form.cleaned_data.get('email')
            email_sent = send_confirmation_email(user_email)
            
            if email_sent:
                return redirect('login')  # Redirect to login page after successful registration
            else:
                return render(request, 'registration/register.html', {'form': form, 'error': 'Failed to send confirmation email.'})
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
