from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from department.forms import FirefighterCreateForm, FirefighterUpdateForm
from department.models import Strazacy


class FirefighterListView(ListView):
    template_name = 'department/firefighter_list.html'
    model = Strazacy
    ordering = ('pk',)


class FirefighterCreateView(CreateView):
    template_name = 'department/firefighter_form.html'
    model = Strazacy
    form_class = FirefighterCreateForm
    success_url = reverse_lazy('firefighter-list')

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
            "go_back": reverse('firefighter-list')
        })
        return context


class FirefighterDetailView(DetailView):
    template_name = 'department/firefighter_detail.html'
    model = Strazacy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('firefighter-list')
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
    success_url = reverse_lazy('firefighter-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('firefighter-detail', args=(self.kwargs['pk'],))
        })
        return context
