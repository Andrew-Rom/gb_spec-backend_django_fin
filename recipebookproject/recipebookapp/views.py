from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import logging

from .forms import SignInForm, SignUpForm

# from .models import Recipe
# from .forms import RecipeForm

logger = logging.getLogger(__name__)


def log_this(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        logger.info(f'Func "{f.__name__}" was called')
        return res

    return wrapper


@log_this
def index(request):
    print(request.user)
    return render(request, "recipebookapp/index.html")


@log_this
def user(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            reg_form = SignUpForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                email = reg_form.cleaned_data['email']
                password = reg_form.cleaned_data['password1']
                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Форма регистрации заполнена неверно')
        elif 'login' in request.POST:
            login_form = SignInForm(request.POST)
            if login_form.is_valid():
                if user := authenticate(request, **login_form.cleaned_data):
                    login(request, user)
                    return redirect('/')
                messages.error(request, 'Ошибка авторизации')
            else:
                messages.error(request, 'Введены неверные данные')

    reg_form = SignUpForm()
    login_form = SignInForm()

    context = {
        'reg_form': reg_form,
        'login_form': login_form
    }
    return render(request, 'recipebookapp/user.html', context)


# def user_register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'user.html', context)
#
#
# def user_login(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#     else:
#         form = SignInForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'user.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


# def home(request):
#     recipes = Recipe.objects.order_by('?')[:5]
#     context = {
#         'recipes': recipes
#     }
#     return render(request, 'home.html', context)
#
# def recipe_detail(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     context = {
#         'recipe': recipe
#     }
#     return render(request, 'recipe_detail.html', context)
#
# def recipe_add(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = RecipeForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'recipe_add.html', context)
#
# def recipe_edit(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = RecipeForm(instance=recipe)
#     context = {
#         'form': form
#     }
#     return render(request, 'recipe_edit.html', context)

