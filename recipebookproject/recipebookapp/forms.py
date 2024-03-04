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


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'placeholder': 'Пароль'}),
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email
