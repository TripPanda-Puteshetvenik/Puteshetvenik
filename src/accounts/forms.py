from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Имейл')
    first_name = forms.CharField(max_length=50, required=False, label='Име')
    last_name = forms.CharField(max_length=50, required=False, label='Фамилия')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Потребителско име'
        self.fields['password1'].label = 'Парола'
        self.fields['password2'].label = 'Потвърди паролата'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'website']
        labels = {
            'avatar': 'Снимка на профила',
            'bio': 'За мен',
            'location': 'Местоположение',
            'website': 'Уебсайт',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'email': 'Имейл',
        }
