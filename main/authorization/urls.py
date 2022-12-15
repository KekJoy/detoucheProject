from django.urls import path
from . import views
from .views import FORMS

urlpatterns = [
    path('', views.MultiStepFormSubmission.as_view(FORMS), name='registration_home'),
]