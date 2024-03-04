from django.conf.urls.static import static
from django.urls import path

from recipebookproject import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('user/', views.user, name='user'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)