from django.conf.urls import url
from django.contrib.auth import views as auth_views
from  WebTool.Views import LoginView


urlpatterns = [
    url(r'^$', LoginView.Index),
    url(r'^Index', LoginView.Index),
]
