from django.db import models
from django.utils import timezone 

# Create your models here.

class MeetingRoom(models.Model):
	reservation_status_choices = (
			('ND', 'No Disponible'),
			('D', 'Disponible'),
			('R', 'Reservada'),
			('C', 'Confirmada')
		)
	name 	 = models.CharField(max_length=30)
	location = models.CharField(max_length=250)
	capacity = models.IntegerField()
	schedule = models.DateField(default=timezone.now)
	# supplies = models.MultipleChoiceField()
	reservation_status = models.CharField(choices=reservation_status_choices, max_length=30)

class Reservation(models.Model):
	reservation_date  = models.DateField(default=timezone.now)
	from_date 		  = models.DateField(default=timezone.now)
	to_date 		  = models.DateField(default=timezone.now)
	assistants 		  = models.IntegerField(default=0)
	supplies_quantity = models.IntegerField(default=0)

class ReservationRequest(models.Model):
	request_date = models.DateField(default=timezone.now)
	approved = models.NullBooleanField()
