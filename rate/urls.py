from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/', views.main),
    url(r'^rate/', views.preference_list),
    url(r'^recommendation/', views.recommendation_list),
    url(r'^login/', views.login_view),
    url(r'^logout/', views.logout_view),
]
