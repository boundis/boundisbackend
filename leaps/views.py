from django.shortcuts import render
from leaps import models

def showLeaps(selected_group):
                leap_list = models.leaps.objects.filter(~Q(group=selected_group))
                leaps = []
                for leap in leap_list:
                        leaps.extend([leaps.message])
                return leaps


