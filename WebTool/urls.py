from django.conf.urls import url
from django.contrib.auth import views as auth_views
from  WebTool.Views import LoginView,ModeView,Rotation,ServerMonitor,ServerManger


urlpatterns = [
    url(r'^$', LoginView.Index),
    url(r'^Index', LoginView.Index),
    url(r'^LoginMain', LoginView.LoginMain),
    url(r'^LogOut', LoginView.LogOut),
    url(r'^getselectserverurl', LoginView.getselectserverurl),
    url(r'^ModeView', ModeView.ModeView),
    url(r'^RotationView', Rotation.RotationView),
    url(r'^ServerMonitorView', ServerMonitor.ServerMonitorView),
    url(r'^GameServerTableNew', ServerManger.NewServerTableVeiw),
    url(r'^FileDownload',ServerManger.FileDownload),
    url(r'^UploadFile',ServerManger.UploadFile),



]
