from django import forms
from .models import Reservation

# Create the form class.
class ReservationForm(forms.Form):
	class Meta:
		model = Reservation	
		fields = ['reservation_date', 'from_date', 'to_date', 'assistants']#, 'room', 'requested_supplies']#'__all__'
