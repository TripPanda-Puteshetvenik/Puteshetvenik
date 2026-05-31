from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    CHOICES = [(i, str(i)) for i in range(1, 6)]

    price = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'star-radio'}), label='Цена')
    location = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'star-radio'}), label='Локация')
    atmosphere = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'star-radio'}), label='Атмосфера')

    class Meta:
        model = Rating
        fields = ['price', 'location', 'atmosphere']
