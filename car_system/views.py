from django.views.generic import ListView, CreateView
from .models import Car, Goal, Ticket
from .forms import TicketForm
from django.urls import reverse_lazy
from fpdf import FPDF
from django.shortcuts import render, redirect
import datetime

class CarList(ListView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_queryset(self):
		time = datetime.datetime.now()
		cars = Car.objects.all()
		for s in cars:
			if s.expire_time.day < time.day and s.expire_time.hour < time.hour:
				s.is_avaliable = False
				s.save()
			elif s.total_chairs == 0:
				s.is_avaliable = False
				s.save()
		return Car.objects.filter(is_avaliable=True)

def ticket_create(request, pk):
	form = TicketForm()
	context = {
		'form' : form
	}
	car = Car.objects.get(id=pk)
	if request.method == "POST":
		form = TicketForm(request.POST)
		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.car = car
			ticket.save()
			get_ticket = Ticket.objects.latest('id')
			return redirect(f"{get_ticket.ticket_pdf.url}")
	return render(request, 'home/ticket_form.html', context)


