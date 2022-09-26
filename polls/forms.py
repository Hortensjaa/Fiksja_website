from django import forms

from .models import Question, Choice


class NewQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class RawNewQuestion(forms.Form):
    question_text = forms.CharField(widget=forms.TextInput(
        attrs={'size': '120', 'id': 'q1',
               'placeholder': 'twoje pytanie pojawi się jako opcja w ankiecie - pytaj o co chcesz ;)'}),
        label='Twoje pytanie:')


class NewChoice(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


class RawNewChoice(forms.Form):
    choice_text = forms.CharField(widget=forms.TextInput(
        attrs={'size': '120', 'id': 'ch1', 'placeholder': 'no słucham, co masz mądrego do powiedzenia?'}),
        label='Twoja odpowiedź')
