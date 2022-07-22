from django.db.models.signals import pre_save, post_save, post_delete
from .models import Car, Goal, Ticket
import io

from django.core.files.base import ContentFile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def ticket_created(sender, instance, created, **kwargs):
	if created:
		ticket = instance
		get_car = Car.objects.get(id=ticket.car.id)
		ticket.chair_number = get_car.total_chairs
		# Generate PDF file
		buf = io.BytesIO()
		canv = canvas.Canvas(buf, pagesize=letter, bottomup=0)
		textob = canv.beginText()
		textob.setTextOrigin(inch, inch)
		textob.setFont("Helvetica", 14)
		lines = [
			f"Name : {ticket.first_name}",
			f"last_name : {ticket.last_name}",
			f"Phone Number : {ticket.phone_number}",
			f"Chair Number : {ticket.chair_number}",
			f"Car Name : {ticket.car.name}",
			f"goal : {ticket.car.goal}",
			f"Time : {ticket.car.expire_time}",
			f"price : {ticket.car.price}",
		]
		for line in lines:
			textob.textLine(line)
		canv.drawText(textob)
		canv.showPage()
		canv.save()
		buf.seek(0)
		pdf = buf.getvalue()
		buf.close()

		my_object = Ticket.objects.latest("id")
		my_object.ticket_pdf.save(f"{ticket.first_name} {ticket.last_name}.pdf", ContentFile(pdf))

		# ----------------------
		get_car.total_chairs -= 1
		get_car.chairs += 1
		get_car.save()

post_save.connect(ticket_created, Ticket)

def ticket_delete(sender, instance, **kwargs):
	ticket = instance
	get_car = Car.objects.get(id=ticket.car.id)
	get_car.total_chairs += 1
	get_car.chairs -= 1
	get_car.save()

post_delete.connect(ticket_delete, Ticket)

