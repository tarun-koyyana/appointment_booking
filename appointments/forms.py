from django import forms
from .models import Appointment, Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time', 'notes']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'contact']
