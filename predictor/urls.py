from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('genreResult/', views.model_form_upload, name='genreResult'),
    path('RecognizerResult/', views.recognize_song, name='RecognizerResult'),
]
