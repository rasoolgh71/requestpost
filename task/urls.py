from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^is_disk$', views.is_disk, name='is_disk'),
    url(r'^show/$', views. MessageListView.as_view(), name='show'),
    url(r'^send/$', views.GenerateRandomMessageView.as_view(), name='send'),
]

