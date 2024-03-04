from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from recipebookapp.models import CustomUser


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=500,
                            label="Наименование блюда",
                            widget=forms.TextInput(attrs={'class': 'recipe-form__title'}))
    description = forms.CharField(max_length=1000,
                                  label="Описание блюда",
                                  widget=forms.Textarea(attrs={'class': 'recipe-form__description'}))
    cooking_steps = forms.CharField(max_length=10000,
                                    label="Как приготовить",
                                    widget=forms.Textarea(attrs={'class': 'recipe-form__cooking'}))
    cooking_time = forms.IntegerField(min_value=1, label="Время приготовления")
    image = forms.ImageField(required=False, label="Изображение блюда")


class SignInForm(AuthenticationForm):
    username = forms.CharField(min_length=2,
                               max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=2,
                               max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email
