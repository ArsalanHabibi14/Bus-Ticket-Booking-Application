from django.urls import path
from . import views

urlpatterns = [
	path('', views.CarList.as_view(), name='CarList'),
	path('ticket/<int:pk>/', views.ticket_create, name='ticket_create_view')
]