from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from bugger.models import create_bug_form
from bugger.models import Bug

@login_required
def create_bug(request):
	User=request.user
	form = create_bug_form()
	if request.method=='POST':
		form = create_bug_form(request.POST)
		if form.is_valid():
			bug=form.save(User)
			form = create_bug_form()
		else:
			form = create_bug_form()
	return render(request, 'create_bug.html', {'form': form})

def listBugs(request):
	if request.user.is_authenticated():
		bug_list = Bug.objects.all()
	return render(request, 'bug_list.html', { 'bug_list':bug_list})
