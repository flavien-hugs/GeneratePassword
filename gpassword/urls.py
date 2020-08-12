from django.urls import path
from gpassword.views import generate

app_name = 'gpwd'
urlpatterns = [
    path('', generate, name='password')]
