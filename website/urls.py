__author__ = 'Prashant'
from django.conf.urls import url,include
from .import views
urlpatterns = [
    url(r'^index',views.index,name="index"),
    url(r'logindata',views.logindata,name="logindata"),
    url(r'login',views.login,name="login"),
    url(r'savedata',views.savedata,name="savedata"),
    url(r'facreg',views.facreg,name="facreg"),
    url(r'about',views.about,name='about'),
    url(r'getarea', views.getarea, name='getarea'),
    url(r'signout',views.signout,name="signout"),
    url(r'upload',views.upload,name="upload"),
    url(r'daol',views.daol,name="daol"),
    url(r'event',views.event,name="event"),
    url(r'adde',views.adde,name="adde"),
    url(r'eins',views.eins,name="eins"),
    url(r'notification',views.notification,name="notification"),
    url(r'disnot',views.disnot,name="disnot"),
    url(r'searche',views.searche,name="searche"),
    url(r'ventreg',views.ventreg,name="ventreg"),
    url(r'avedata',views.avedata,name="avedata"),
    url(r'^importfile',views.importfile,name="importfile"),
    url(r'^contact',views.contact,name="contact"),
    url(r'^download', views.download, name='download'),


]
