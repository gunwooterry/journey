from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Destination
import random


def main(request):
    if request.user.is_authenticated:
        data = {'user': request.user}
    else:
        data = {'user': None}
    return render(request, 'main.html', data)


def login_view(request):
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
def preference_list(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    dest_list = Destination.objects.all()
    for dest in dest_list:
        score = int(request.POST.get('rating_'+dest.name, -1))
        userprofile.set_preference(dest.name, score)
    data = {'user': user,
            'pref_list': userprofile.preferences.all()}
    return render(request, 'rate.html', data)


@login_required
def recommendation_list(request):
    user = request.user
    dest_list = Destination.objects.all()
    recommendations = []
    recommendations.append(random.choice(dest_list))
    recommendations.append(random.choice(dest_list))
    recommendations.append(random.choice(dest_list))
    data = {'user': user,
            'rec_list': recommendations}
    return render(request, 'recommendation.html', data)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/main/')
