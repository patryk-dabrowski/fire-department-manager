from django.views import View
from django.views.generic.base import TemplateResponseMixin

from department.models import Pojazdy


class VehicleView(TemplateResponseMixin, View):
    template_name = 'department/vehicle.html'

    def get(self, request):
        vehicles = Pojazdy.objects.all()
        return self.render_to_response({"vehicles": vehicles})
