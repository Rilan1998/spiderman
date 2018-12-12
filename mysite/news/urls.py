from django.urls import path

from . import views
app_name = 'news'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('<int:id>/', views.DetailView.as_view(), name='detail'),
]

