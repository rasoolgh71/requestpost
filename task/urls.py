from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'index$', views.IndexView.as_view(), name='index'),
    #url(r'send$', views.send, name='send'),
    #url(r'show$', views.show, name='show'),
    url(r'^home$', views.home, name='home'),
   # url(r'^is_disk$', views.is_disk, name='is_disk'),
    url(r'^show/$', views.UsersListView.as_view(), name='show'),
    url(r'^send/$', views.GenerateRandomUserView.as_view(), name='send'),
]

