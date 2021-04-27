from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from department.models import Strazacy


class FirefighterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=150, label='Imie')
    last_name = forms.CharField(required=True, max_length=150, label='Nazwisko')
    username = forms.CharField(required=True, max_length=150, label='Nazwa użytkownika')
    email = forms.EmailField(required=True)

    class Meta:
        model = Strazacy
        fields = ('first_name', 'last_name', 'username', 'email', 'data_urodzenia', 'data_wstapienia',
                  'ostatnie_badanie', 'nastepne_badanie', 'ubezpieczenie', 'kierowca', 'termin_prawa_jazdy',
                  'termin_wkladki', 'termin_kpp', 'ostatnia_skladka', 'status', 'uwagi',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['username'].initial = self.instance.user.username
        self.fields['email'].initial = self.instance.user.email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Użytkownik z taką nazwą użytkownika już istnieje')
        return username


class FirefighterCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=150, label='Imie')
    last_name = forms.CharField(required=True, max_length=150, label='Nazwisko')
    username = forms.CharField(required=True, max_length=150, label='Nazwa użytkownika')
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=128, label='Hasło',
                               widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
    password_repeat = forms.CharField(required=True, max_length=128, label='Powtórz hasło',
                                      widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

    class Meta:
        model = Strazacy
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password_repeat', 'data_urodzenia',
                  'data_wstapienia', 'ostatnie_badanie', 'nastepne_badanie', 'ubezpieczenie', 'kierowca',
                  'termin_prawa_jazdy', 'termin_wkladki', 'termin_kpp', 'ostatnia_skladka', 'status', 'uwagi',)

    def clean(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise ValidationError('Hasła muszą być takie same.', )
        return super().clean()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Użytkownik z taką nazwą już istnieje')
        return username
