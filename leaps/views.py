from django.shortcuts import render
from leaps import models

@login_required
def create_group(request):
	User = request.user
	form = models.leap_form(request.POST)
	if form.is_valid():
		group=form.save()

