from django.conf.urls.static import static
from django.urls import path

from recipebookproject import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('logout/', views.user_logout, name='logout'),
    path('cooker/', views.cooker, name='cooker'),
    path('recipe_add/', views.recipe_add, name='recipe_add'),
    path('recipe_edit/<int:recipe_id>', views.recipe_edit, name='recipe_edit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)