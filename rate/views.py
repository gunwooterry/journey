from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def main(request):
    if request.user.is_authenticated:
        profile = {'user': request.user}
    else:
        profile = {'user': None}
    return render(request, 'main.html', profile)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/main/')
    return render(request, 'login.html')


@login_required
def preferenceList(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    pref = {'preferences': userprofile.preferences}
    return render(request, 'rate.html', pref)


@login_required
def logoutView(request):
    logout(request)
    return redirect('/main/')
