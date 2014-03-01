from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from user_profiles.models import UserProfile
from datetime import date
from teams.models import Membership
from django.db.models import Q
from django.contrib.auth.models import User
from user_profiles import forms

# Create your views here.
def index(request):
    return render_to_response("index.html",
                              RequestContext(request))
@login_required
def my_profile(request):
    User = request.user
    profile = User.profile
    person= profile.user
    membership_list = Membership.objects.filter(person=person)
    if profile.dob:
        today = date.today()
        birthday = profile.dob
        age = today.year - birthday.year
        if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
            age -= 1
        return render(request, 'user_profiles/myprofile.html', {'person_object': profile, 'age':age, 'membership_list':membership_list})
    return render(request, 'user_profiles/myprofile.html', {'person_object': profile, 'membership_list':membership_list})

@login_required
def user_profile(request, user_id):
    profile = UserProfile.objects.get(user=user_id)
    #persons = Person.objects.filter(~Q(user=User))
    User= profile.user
    membership_list = Membership.objects.filter(person=user_id)
    if profile.dob:
        today = date.today()
        birthday = profile.dob
        age = today.year - birthday.year
        if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
            age -= 1
        return render(request, 'user_profiles/userprofile.html', {'profile': profile, 'age':age, 'membership_list':membership_list})
    return render(request, 'user_profiles/userprofile.html', {'profile': profile, 'membership_list':membership_list})

@login_required
def edit_UserProfile(request):
    User = request.user.profile
    user = request.user
    form = forms.UserProfileForm(instance=User)
    form1= forms.UserForm(instance=user)
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, request.FILES, instance=User)
        form1 = forms.UserForm(request.POST, request.FILES, instance=user)
        if form1.is_valid() and form.is_valid:
            form.save()
            form1.save()
            return HttpResponseRedirect('/profile/myprofile.html')
        else:
            error=True
            return render(request, 'user_profiles/editprofile.html', {'form': form, 'error':error, 'form': form, 'form1': form1})
    else:
        return render(request, 'user_profiles/editprofile.html', {'form': form, 'form1': form1})




