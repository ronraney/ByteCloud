from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.byte_list, name='byte_list'),
]
