from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from bugger.models import create_bug_form, edit_bug_form
from bugger.models import Bug
from django.http import HttpResponseRedirect
from leaps.models import Leap, leap_form_bug

@login_required
def create_bug(request):
	User=request.user
	form = create_bug_form()
	if request.method=='POST':
		form = create_bug_form(request.POST)
		if form.is_valid():
			bug=form.save(User)
			form = create_bug_form()
			return HttpResponseRedirect('/bugger')
		else:
			form = create_bug_form()
	return render(request, 'create_bug.html', {'form': form})

@login_required
def listBugs(request):
	if request.user.is_authenticated():
		User = request.user
		bug_list = Bug.objects.all()
	return render(request, 'bug_list.html', { 'bug_list':bug_list, 'User':User})
@login_required
def listBugsOwner(request):
	if request.user.is_authenticated():
		User = request.user
		print User.username
		bug_list = Bug.objects.filter(assigned_to=User)
		for bug in bug_list:
			print bug.assigned_to
	return render(request, 'bug_list_assigned.html',{ 'bug_list':bug_list})

@login_required
def bugDetail(request,bug_id):
	bug = Bug.objects.get(pk=bug_id)
	User = request.user
	leap_list = Leap.objects.filter(bug=bug).order_by('-created_at')
	form = leap_form_bug()
	if request.method == 'POST':
		form = leap_form_bug(request.POST)
		if form.is_valid():
			form.save(bug,User)
			form = leap_form_bug()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	return render(request, 'bug_detail.html', {'bug':bug, 'leap_list':leap_list, 'form':form})

@login_required
def editBug(request, bug_id):
	bug = Bug.objects.get(pk=bug_id)
	User = request.user
	form = edit_bug_form(instance=bug)
	if request.method=='POST':
		form = edit_bug_form(request.POST, instance=bug)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/bugger/bug/%i/' % bug.id)
			
	return render(request, 'edit_bug.html', {'bug':bug, 'form':form})
	
