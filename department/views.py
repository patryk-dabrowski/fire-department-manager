from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.base import TemplateResponseMixin, View

from .forms import FirefighterUpdateForm, FirefighterCreateForm
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
    template_name = 'department/firefighter_form.html'
    model = Strazacy
    form_class = FirefighterCreateForm
    success_url = reverse_lazy('firefighter')

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('firefighter')
        })
        return context


class FirefighterDetailView(DetailView):
    template_name = 'department/firefighter_detail.html'
    model = Strazacy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('firefighter')
        })
        return context


class FirefighterUpdateView(UpdateView):
    template_name = 'department/firefighter_form.html'
    model = Strazacy
    form_class = FirefighterUpdateForm

    def get_success_url(self):
        return reverse('firefighter-detail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        instance = form.save()
        instance.user.first_name = form.cleaned_data.get('first_name')
        instance.user.last_name = form.cleaned_data.get('last_name')
        instance.user.username = form.cleaned_data.get('username')
        instance.user.email = form.cleaned_data.get('email')
        instance.user.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('firefighter-detail', args=(self.kwargs['pk'],))
        })
        return context


class FirefighterDeleteView(DeleteView):
    model = Strazacy
    template_name = 'department/firefighter_confirm_delete.html'
    success_url = reverse_lazy('firefighter')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('firefighter-detail', args=(self.kwargs['pk'],))
        })
        return context
