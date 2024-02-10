
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    submit_button = forms.CharField(widget=forms.HiddenInput(), required=False)