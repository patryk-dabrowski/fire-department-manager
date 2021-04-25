from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.base import TemplateResponseMixin, View

from .forms import FirefighterCreate
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


class VehicleView(TemplateResponseMixin, View):
    template_name = 'department/vehicle.html'

    def get(self, request):
        vehicles = Pojazdy.objects.all()
        return self.render_to_response({"vehicles": vehicles})


class FirefighterView(ListView):
    template_name = 'department/firefighter_list.html'
    model = Strazacy
    ordering = ('pk',)


class FirefighterCreateView(CreateView):
    pass


class FirefighterDetailView(DetailView):
    pass


class FirefighterUpdateView(UpdateView):
    template_name = 'department/firefighter_form.html'
    model = Strazacy
    form_class = FirefighterCreate

    def get_success_url(self):
        return reverse('firefighter-detail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        instance = form.instance
        instance.user.first_name = form.cleaned_data.get('first_name')
        instance.user.last_name = form.cleaned_data.get('last_name')
        instance.user.email = form.cleaned_data.get('email')
        instance.user.save()
        return super().form_valid(form)



class FirefighterDeleteView(DeleteView):
    pass
