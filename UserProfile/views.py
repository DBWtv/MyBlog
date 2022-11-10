from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegUserProfile
from .models import UserProfile
from django.urls import reverse_lazy


def profile_veiw(request):
    user = request.user
    if user.id==None:
        return redirect('login')
    else:
        profile = UserProfile.objects.filter(user_id = user)
        context = {
            'profile': profile,
        }
        return render(request, 'PfPj/profile.html', context)


def reg_user(request):
    user = request.user
    if user.id == None:
        return redirect('login')
    else:
        if request.method == "POST":
            form = RegUserProfile(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user_id = request.user
                instance.save()
                return redirect('home')
        else:
            form = RegUserProfile()
        context = {
            "form": form
        }
        return render(request, 'PfPj/new_profile.html', context)