from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].label = 'Nazwa użytkownika:'
        self.fields['email'].help_text = '* podaj jeśli chcesz, nie będę spamować ;)'
        self.fields['password1'].help_text = 'To jest serwer na hoście za 2 złote... nie używaj tu' \
                                             ' swojego hasła do wszystkiego, tylko najlepiej wygeneruj' \
                                             ' jakieś losowe'
        self.fields['password1'].label = 'Hasło:'
        self.fields['password2'].help_text = None
        self.fields['password2'].label = 'Jeszcze raz hasło:'

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
