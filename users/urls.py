from django.urls import path
from .views import PeopleView, AboutVew, PeopleCreatView


urlpatterns = [
    path('', PeopleCreatView.as_view(), name='people'),
    path('about/', AboutVew.as_view(), name='about')
]