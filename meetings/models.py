from django.db import models
from django.utils import timezone 
from django.utils.encoding import smart_text
from django.db.models.signals import post_save

# Create your models here.

class MeetingRoom(models.Model):
	reservation_status_choices = (
			('ND', 'No Disponible'),
			('D', 'Disponible'),
			('R', 'Reservada'),
			('C', 'Confirmada')
		)

	def default_supplies():
		''' Return the default supplies for a room'''
		projector, _ = Supply.objects.get_or_create(supply_name='Proyector')
		board, _ =  Supply.objects.get_or_create(supply_name='Pizarra')
		return [projector, board]

	name 	 		   = models.CharField(max_length=30)
	location 		   = models.CharField(max_length=250)
	capacity 		   = models.IntegerField()
	schedule 		   = models.DateField(default=timezone.now)
	supplies		   = models.ManyToManyField('Supply', blank=True, default=default_supplies)
	reservation_status = models.CharField(choices=reservation_status_choices, max_length=30, default='D')

	def __str__(self): 
		return smart_text(self.name)

class Supply(models.Model):
	supply_name 		= models.CharField(max_length=30)
	supply_remaining    = models.IntegerField(default=1)
	supply_total    	= models.IntegerField(default=1)

	def __str__(self): 
		return smart_text(self.supply_name)

class Reservation(models.Model):
	reservation_date   = models.DateTimeField(default=timezone.now)
	from_date 		   = models.DateTimeField(default=timezone.now)
	to_date 		   = models.DateTimeField(default=timezone.now)
	assistants 		   = models.IntegerField(default=0)
	room 			   = models.ForeignKey(MeetingRoom, related_name='reservation_of')
	requested_supplies = models.ManyToManyField(Supply, through='SupplyDetail')

	def __str__(self): 
		return 'Reserva hecha en la fecha {}'.format(self.reservation_date)

class SupplyDetail(models.Model):
	supply 		= models.ForeignKey(Supply, on_delete=models.CASCADE, related_name='supply_of')
	reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation_of')
	quantity 	= models.IntegerField(default=1)

class ReservationRequest(models.Model):
	request_date = models.DateField(default=timezone.now)
	approved     = models.NullBooleanField()

def reservation_model_post_save_receiver(sender, instance, *args, **kwargs):
    #if not 'Pizarra' in instance.requested_supplies and instance.title:
    print(instance.requested_supplies)
    print(args)
    print(kwargs) 
    print(sender)

post_save.connect(reservation_model_post_save_receiver, sender=Reservation)