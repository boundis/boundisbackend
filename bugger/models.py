from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

STATUS_CHOICES = (
        ('assigned', 'Assigned'),
        ('pending', 'Pending'),
	('fixed', 'Fixed'),
	('nofix', 'Will Not Fix'),
)
PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
)
class Bug(models.Model):
	summary = models.CharField(max_length=100)
	bug_description = models.CharField(max_length=2000)
	assigned_to = models.ForeignKey(User,related_name='bug_work_assigned_to',blank=True,null=True)
	created_by = models.ForeignKey(User,related_name='bug_created_by')
	status = models.CharField(choices=STATUS_CHOICES,max_length=100,blank=True,null=True)
	priority = models.CharField(choices=PRIORITY_CHOICES,max_length=100)
	created_on = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
              return self.summary
class create_bug_form(forms.Form):
	summary = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 1}),required=True)
	bug_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 20}),required=True)
	priority = forms.ChoiceField(widget=forms.Select, choices=PRIORITY_CHOICES)
	def save(self,user):
		new_bug = Bug(summary=self.cleaned_data['summary'],bug_description=self.cleaned_data['bug_description'],priority=self.cleaned_data['priority'],created_by=user,)
		new_bug.save()
		return new_bug.id		

class edit_bug_form(ModelForm):
	class Meta:
		model = Bug
		fields = ['summary','priority','status','assigned_to']

#class edit_bug_form(forms.Form):
#	user_list = User.objects.all()
 #       summary = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 1}),required=True)
  #      bug_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 20}),required=True)
   #     priority = forms.ChoiceField(widget=forms.Select, choices=PRIORITY_CHOICES)
#	status = forms.ChoiceField(widget=forms.Select, choices=STATUS_CHOICES)
#	assigned_to = forms.ModelChoiceField(queryset=user_list)
#	def save(self,bug):
#		bug_id = bug.id
#		bug = Bug.objects.filter(pk=bug_id)
#		bug.summary = self.cleaned_data['summary']
#		bug.bug_description = self.cleaned_data['bug_description']
#		bug.priority = self.cleaned_data['priority']
#		bug.status = self.cleaned_data['status']
#		bug.assigned_to = self.cleaned_data['assigned_to']
#		bug.save()
#		return bug.id	
