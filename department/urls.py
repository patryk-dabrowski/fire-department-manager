from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sprzet/', views.EquipmentView.as_view(), name='equipment'),
    path('pojazdy/', views.VehicleView.as_view(), name='vehicle'),

    path('strazacy/', views.FirefighterView.as_view(), name='firefighter'),
    path('strazacy/nowy/', views.FirefighterCreateView.as_view(), name='firefighter-create'),
    path('strazacy/<int:pk>/', views.FirefighterDetailView.as_view(), name='firefighter-detail'),
    path('strazacy/<int:pk>/edycja/', views.FirefighterUpdateView.as_view(), name='firefighter-update'),
    path('strazacy/<int:pk>/usun/', views.FirefighterDeleteView.as_view(), name='firefighter-delete'),
]
