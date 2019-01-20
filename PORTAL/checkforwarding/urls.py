# checkforwarding/urls.py
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
app_name='checkforwarding'

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
]