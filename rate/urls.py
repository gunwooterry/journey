from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/', views.main),
    url(r'^rate/', views.preference_list),
    url(r'^recommendation/', views.recommendation_list),
    url(r'^signup/', views.signup_view),
    url(r'^signin/', views.signin_view),
    url(r'^logout/', views.logout_view),
]
