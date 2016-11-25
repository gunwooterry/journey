from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/', views.main),
    url(r'^rate/', views.preferenceList),
    url(r'^login/', views.loginView),
    url(r'^logout/', views.logoutView),
]
