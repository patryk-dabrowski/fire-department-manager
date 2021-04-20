from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sprzet/', views.EquipmentView.as_view(), name='equipment'),
    path('pojazdy/', views.VehicleView.as_view(), name='vehicle'),
    path('strazacy/', views.FirefighterView.as_view(), name='firefighter'),
]
