from django.db import models 

class Goal(models.Model):
	province = models.CharField(max_length=200)
	goal_province = models.CharField(max_length=120)

	def __str__(self):
		return f'{self.province} - {self.goal_province}'


class Car(models.Model):
	name = models.CharField(max_length=200)
	total_chairs = models.IntegerField(default=0)
	chairs = models.IntegerField(default=0)
	goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
	expire_time = models.DateTimeField()
	price = models.DecimalField(max_digits=10, decimal_places=2, default=500)
	is_avaliable = models.BooleanField(default=True)
	def __str__(self):
		return self.name



class Ticket(models.Model):
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=150)
	phone_number = models.CharField(max_length=50)
	ticket_pdf = models.FileField(upload_to='ticket/', null=True, blank=True)
	chair_number = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
