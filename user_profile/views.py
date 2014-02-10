from django.shortcuts import render
from user_profile import models
from user_profile.models import Person
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

def add_user(request):
    form = models.user_form()
    if request.method == 'POST':
        form = models.user_form(request.POST)
        if form.is_valid():
            form.save()
            form = models.user_form(request.POST)
            return HttpResponseRedirect('/teams/login')
    return render(request, 'add_user.html', {'form': form })

@login_required
def user_profile(request):
    User = request.user
    #persons = Person.objects.filter(~Q(user=User))
    persons = Person.objects.get(user=User.id)
    return render(request, 'profile.html', {'person_object': persons})