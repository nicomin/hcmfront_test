from django.contrib import admin
from .models import (
		MeetingRoom,
		Reservation,
		ReservationRequest,
		Supply,
		SupplyDetail
	)

# Register your models here.

class SupplyDetailInline(admin.TabularInline):
	''' Display this intermediate model in the admin'''
	model = SupplyDetail
	extra = 1

class SupplyAdmin(admin.ModelAdmin):
	inlines = (SupplyDetailInline,) 

class ReservationAdmin(admin.ModelAdmin):
	inlines = (SupplyDetailInline,)

admin.site.register(MeetingRoom)
admin.site.register(ReservationRequest)
admin.site.register(Reservation, ReservationAdmin) 
admin.site.register(Supply, SupplyAdmin) 
admin.site.register(SupplyDetail)

