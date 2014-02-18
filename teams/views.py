from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
from user_profile import models
from teams import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from leaps.models import leap_form
@login_required
def listMembership(request):
	if request.user.is_authenticated():
		User = request.user
		per = models.Person.objects.filter(~Q(user=User))
		membership_list = models.Membership.objects.filter(~Q(person=per))	
	return render(request, 'teams.html', {'membership_list' : membership_list})

def listMembershipList(User):
		per = models.Person.objects.filter(~Q(user=User))
		membership_list = models.Membership.objects.filter(~Q(person=per))
		group_list = []
		for membership in membership_list:
			group_list.extend([membership.group.group_name])
		return group_list
		
def isOwner(person_obj,group_obj):
	membership_obj = models.Membership.objects.get(group=group_obj,person=person_obj)
	if membership_obj.membership_type=='owner':
		print membership_obj.membership_type
		return True
	else:
		print membership_obj.membership_type
		return False
		
@login_required
def group_detail(request, group_id): 
    group = models.Group.objects.get(pk=group_id)
    User = request.user
    persons = models.Person.objects.get(user=User.id)
    memlist = listMembershipList(User)
    if group.group_name not in memlist:
            return HttpResponse("You are not authorized to view this group.")
    else:
	auth = isOwner(persons,group)
    print auth
    if auth == True:
        form = models.add_member_form()
	form2 = leap_form()
	if request.method == 'POST':
            form = models.add_member_form(request.POST)
	    form2 = leap_form(request.POST)
            if form.is_valid():
			    form.save(group)
			    form = models.add_member_form()
	    else:
                form = models.add_member_form()
            return render(request, 'group_detail.html', {'group': group,'form':form,'form2':form2})
        else:	
             return render(request, 'group_detail.html', {'group': group,'form':form})			
    else:
         print "NOT AUTH"
	 form2 = leap_form()
         if request.method == 'POST':
	 	form2 = leap_form(request.POST)
		if form2.is_valid():
			form2.save(group,User)
			form2 = leap_form()
	 return render(request, 'group_detail.html', {'group': group, 'form2':form2})

@login_required
def create_group(request):
    User=request.user
    persons = models.Person.objects.get(user=User.id)
    form = models.group_form()
    if request.method == 'POST':
        form = models.group_form(request.POST)
        if form.is_valid():
            group=form.save(persons)
            form = models.group_form()
        else:
            form = models.group_form()
    return render(request, 'create_group.html', {'form': form })
