from django.conf.urls import url

from . import views

app_name = "Svasth"

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^(?P<UserID>[0-9]+)/MyDoctors/', views.MyDocters, name="MyDoctors"),
    url(r'^LogIn/', views.LogIn, name='LogIn'),
    url(r'^SignIn/', views.SignIn, name='SignIn'),
    url(r'^(?P<UserID>[0-9]+)/Reports/', views.Reports, name='Reports'),
    url(r'^(?P<UserID>[0-9]+)/Home/', views.home, name='Home'),
    url(r'^(?P<UserID>[0-9]+)/Appointments/', views.Appointments, name='Appointments'),
    url(r'^(?P<UserID>[0-9]+)/Hospital/', views.Hospitals, name='Hospitals'),
    url(r'^(?P<UserID>[0-9]+)/Specialisations/(?P<HopId>[0-9]+)$', views.Special, name='Special'),
    url(r'^(?P<UserID>[0-9]+)/DoctorsSpecial/(?P<SpecId>[0-9]+)$', views.DoctersSpecial, name='DoctoresSpecial'),
    url(r'^Contact/',views.Contacts, name='Contact'),
]
