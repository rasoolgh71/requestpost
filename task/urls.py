from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'index$', views.IndexView.as_view(), name='index'),
    url(r'send$', views.send, name='send'),
    url(r'home$', views.home, name='home'),

]
