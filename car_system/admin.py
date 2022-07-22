from django.contrib import admin
from .models import Car, Goal, Ticket

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'total_chairs', 'goal', 'price']

admin.site.register(Goal)

admin.site.register(Ticket)