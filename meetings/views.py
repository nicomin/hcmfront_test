from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.contrib.auth.decorators import login_required

from .forms import ReservationForm
from .models import Reservation

# Create your views here.

class ReservationDeleteView(DeleteView):
	model = Reservation

	def get_success_url(self):
		return reverse("reservation_list")


class ReservationCreateView(SuccessMessageMixin, CreateView):
	template_name = "create_reservation.html"
	model = Reservation	
	fields = '__all__'
	success_message = "%(title)s has been created at %(created_at)s"
	def form_valid(self, form):
		form.instance.added_by = self.request.user
		valid_form = super(BookCreateView, self).form_valid(form)
		messages.success(self.request, "Reservation created!")
		return valid_form

	def get_success_url(self):
		return reverse("reservation_list")

	def get_success_message(self, cleaned_data):
		return self.success_message % dict(
			cleaned_data,
			created_at=self.object.timestamp,
		)


class ReservationUpdateView(UpdateView):
	model = Reservation
	#fields = ["title", "description"]
	form_class = ReservationForm
	template_name = "forms.html"


class ReservationDetail(SuccessMessageMixin, ModelFormMixin, DetailView):
	model = Reservation
	form_class = ReservationForm
	success_message = "%(title)s has been updated."

	def get_context_data(self, *args, **kwargs):
		context = super(ReservationDetail, self).get_context_data(*args, **kwargs)
		context["form"] = self.get_form()
		context["btn_title"] = "Update Reservation"
		return context

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			self.object = self.get_object()
			form = self.get_form()
			if form.is_valid():
				return self.form_valid(form)
			else:
				return self.form_invalid(form)

	def get_success_url(self):
		return reverse("reservation_list")


class ReservationListView(ListView):
	model = Reservation