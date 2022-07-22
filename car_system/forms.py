from django.forms import ModelForm
from .models import Ticket


class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = '__all__'
		exclude = ['car', 'ticket_pdf', 'chair_number']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs.update({"class" : 'form-control'})