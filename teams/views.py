from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
from user_profiles import models
from teams import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from leaps.models import  Leap
from leaps.forms import leap_form
from teams.forms import group_form, add_member_form

@login_required
def listMembership(request):
	if request.user.is_authenticated():
		User = request.user
		membership_list = models.Membership.objects.filter(person=User)	
	return render(request, 'teams/teams.html', {'membership_list' : membership_list})

def listMembershipList(User):
		User = User
		membership_list = models.Membership.objects.filter(person=User)
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
    memlist = listMembershipList(User)
    leap_list = Leap.objects.filter(group=group).order_by('-created_at')
    form2 = leap_form(prefix='postMessage')
    if group.group_name not in memlist:
        return HttpResponse("You are not authorized to view this group.")
    else:
        auth = isOwner(User,group)
        if auth:
            form = add_member_form(prefix='addMember')
            if request.method == 'POST':
                form = add_member_form(request.POST, prefix='addMember' )
                if form.is_valid():
                    new_member = form.save(group)
                    print new_member
                else:	
                    print "tstt"
                    form2 = leap_form(request.POST, prefix ='postMessage')
                    form = add_member_form(prefix='addMember')
                    if form2.is_valid():
                        print "tsttt2"
                        form2.save(group,User)
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    else:
                        form2=leap_form(prefix='postMessage')
            return render(request, 'teams/group_detail.html', {'group': group,'leap_list':leap_list,'form':form,'form2':form2})           
        else:
            print "NOT Owner"
            form2 = leap_form()
            if request.method == 'POST':
                form2 = leap_form(request.POST)
            if form2.is_valid():
                form2.save(group,User)
                form2 = leap_form()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'teams/group_detail.html', {'group': group,'leap_list':leap_list,'form2':form2})  


@login_required
def create_group(request):
    User=request.user
    form = group_form()
    if request.user.is_authenticated():
        membership_list = models.Membership.objects.filter(person=User)
    if request.method == 'POST':
        form = group_form(request.POST)
        if form.is_valid():
            group=form.save(User)
            return HttpResponseRedirect('/teams/group/create')
        else:
            form = group_form()
    return render(request, 'teams/create_group.html', {'form': form, 'membership_list': membership_list })
