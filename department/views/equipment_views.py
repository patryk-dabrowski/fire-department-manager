from django.views.generic import ListView

from department.models import Sprzet


class EquipmentView(ListView):
    template_name = 'department/equipment.html'
    model = Sprzet
    ordering = ('pk',)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('przeglad_sprzet')
