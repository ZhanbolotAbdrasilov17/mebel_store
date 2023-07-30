from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('mail/create/', MailCreateView.as_view(), name='mail_create'),
]