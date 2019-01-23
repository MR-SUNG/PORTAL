# check/urls.py
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
app_name='check'

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
]