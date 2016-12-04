from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Destination
from .utils import recommend


def main(request):
    if request.user.is_authenticated:
        data = {'user': request.user}
    else:
        data = {'user': None}
    return render(request, 'main.html', data)


def signin_view(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/main/')
    return render(request, 'signin.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username=username, password=password,
                                        first_name=first_name,
                                        last_name=last_name, email=email)
        UserProfile.objects.create(user=user)
        login(request, user)
        return redirect('/main/')
    return render(request, 'signup.html')


@login_required
def preference_list(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    for dest in Destination.objects.all():
        score = int(request.POST.get('rating_'+dest.name, -1))
        userprofile.set_preference(dest.name, score)
    pref_list = list(userprofile.preferences.all())
    pref_list.sort(key=lambda x: (x.destination.name, x.destination.country.name))
    data = {'user': user,
            'pref_list': userprofile.preferences.all()}
    return render(request, 'rate.html', data)


@login_required
def recommendation_list(request):
    user = request.user
    recommendations = recommend(user)
    data = {'user': user,
            'rec_list': recommendations}
    return render(request, 'recommendation.html', data)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/main/')
