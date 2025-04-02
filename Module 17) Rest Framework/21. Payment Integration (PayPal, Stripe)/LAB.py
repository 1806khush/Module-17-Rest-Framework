# appointments/models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.patient_name} - {self.doctor.name}'
# appointments/views.py
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Appointment
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        token = request.POST.get('stripeToken')

        try:
            # Create a charge using the Stripe API
            charge = stripe.Charge.create(
                amount=5000,  # Amount in cents, so 5000 = $50
                currency='usd',
                description=f"Appointment with Dr. {appointment.doctor.name}",
                source=token
            )

            # Update the appointment to reflect payment status
            appointment.is_paid = True
            appointment.save()

            messages.success(request, "Payment successful! Your appointment is confirmed.")
            return redirect('appointment_detail', appointment_id=appointment.id)
        except stripe.error.CardError as e:
            messages.error(request, f"Payment failed: {e.user_message}")
            return redirect('checkout', appointment_id=appointment.id)

    return render(request, 'payment/checkout.html', {'appointment': appointment})
