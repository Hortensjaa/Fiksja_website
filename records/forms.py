from django import forms
from datetime import date

from .models import Record, Break
from .categories import CATEGORIES


class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        months = [(month, month) for month in range(1, 13)]
        years = [(year, year) for year in range(2001, date.today().year+1)[::-1]]
        widgets = [
            forms.Select(attrs=attrs, choices=days),
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            year, month, day = value.split('-')
            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        return '{}-{}-{}'.format(year, month, day)


class NewRecord(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'category', 'description']


class RawNewRecord(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '120', 'id': 't1'}), label='Nazwa rekordu')
    category = forms.ChoiceField(choices=CATEGORIES)
    description = forms.CharField(widget=forms.Textarea(
        attrs={"cols": "120", "rows": "10", 'id': 'd1',
               'placeholder': 'To pole nie jest obowiązkowe, ale jeśli opiszesz rekord, będzie '
                              'łatwiej stwierdzić, jak może zostać pobity'}),
        label='Opis', required=False)


class NewBreak(forms.ModelForm):
    class Meta:
        model = Break
        fields = ['value', 'breaker', 'breaker_login', 'break_date', 'current_break']


class RawNewBreak(forms.Form):
    value = forms.CharField(widget=forms.TextInput(
        attrs={'size': '120', 'id': 't1',  'placeholder': 'np. 11 piw, 43 sekundy itp.'}),
        label='Wartość rekordu: ')
    breaker = forms.CharField(widget=forms.TextInput(attrs={'size': '120', 'id': 'b1'}), label='Rekordzista')
    break_date = forms.DateField(widget=DateSelectorWidget(attrs={'id': 'bd1'}), label='Data pobicia')
    breaker_login = forms.CharField(widget=forms.TextInput(
        attrs={'size': '120', 'id': 'bl1',
               'placeholder': 'Jeżeli rekordzista ma konto w serwisie, podaj jego login'}),
        label='Login', required=False)
    # current_break = forms.BooleanField(label='Czy to aktualny rekord?')
