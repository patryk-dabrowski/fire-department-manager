from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin, View

from .models import Pojazdy, Sprzet, Strazacy


class HomeView(TemplateView):
    template_name = 'department/home.html'


class EquipmentView(ListView):
    template_name = 'department/equipment.html'
    model = Sprzet
    ordering = ('pk',)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('przeglad_sprzet')


class FirefighterView(ListView):
    template_name = 'department/firefighter.html'
    model = Strazacy
    ordering = ('pk',)


class VehicleView(TemplateResponseMixin, View):
    template_name = 'department/vehicle.html'

    def get(self, request):
        vehicles = Pojazdy.objects.all()
        return self.render_to_response({"vehicles": vehicles})
