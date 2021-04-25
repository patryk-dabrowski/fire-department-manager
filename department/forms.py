from django import forms

from department.models import Strazacy


class FirefighterCreate(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=150, label='Imie')
    last_name = forms.CharField(required=True, max_length=150, label='Nazwisko')
    email = forms.EmailField(required=True)

    class Meta:
        model = Strazacy
        fields = ('first_name', 'last_name', 'email', 'data_urodzenia', 'data_wstapienia', 'ostatnie_badanie',
                  'nastepne_badanie', 'ubezpieczenie', 'kierowca', 'termin_prawa_jazdy', 'termin_wkladki', 'termin_kpp',
                  'ostatnia_skladka', 'status', 'uwagi',)
        labels = {
            'first_name': 'Imie',
            'last_name': 'Nazwisko',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email
