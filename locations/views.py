from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from locations import models, forms
from django.core.context_processors import csrf
from django.db.models import Q
from sports.models import Sport, Facility_type

def allvenues(request):		
    venue_list = models.Venue.objects.order_by('name')
    venue_piclist = []
    facility_list = []
    for Venue in venue_list:
        venue_piclist.extend(list(models.Venuepic.objects.filter(venue=Venue.id)))
        facility_list.extend(list(models.Facility.objects.filter(venue=Venue.id)))
    context = {'venue_list': venue_list, 'facility_list' : facility_list, 'venue_piclist':venue_piclist,}
    return render(request, 'locations/search_results.html', context)

def venue_detail(request, venue_id):
    Venue = models.Venue.objects.get(pk=venue_id)
    pic_list = models.Venuepic.objects.filter(venue=venue_id)
    if len(pic_list) > 0:
        firstpic = pic_list[0]
    else:
        firstpic = '/media/venue/venueplaceholder.png'
    facility_list = models.Facility.objects.filter(venue=venue_id)
    facility_piclist = []
    for Facility in facility_list:
        facility_piclist.extend(list(models.Facilitypic.objects.filter(facility=Facility.id)))
    context = {'Venue': Venue, 'facility_list' : facility_list, 'pic_list':pic_list, 'firstpic':firstpic, 'facility_piclist':facility_piclist}
    return render(request, 'locations/venue_detail.html', context)

def add_venue(request):
    form = forms.venue_form()
    formpic= forms.venuepic_form()
    if request.method == 'POST':
        form = forms.venue_form(request.POST)
        formpic= forms.venuepic_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            if formpic.is_valid():
                venue=instance.save()
                instancepic=formpic.save(commit=False)
                instancepic.venue = instance
                instancepic.save()
            return HttpResponseRedirect('/locations/%i/' %instance.id)

        else:
            error = True
            return render(request, 'locations/add_venue.html', {'form': form, 'formpic':formpic, 'error':error})
    else:
        return render(request, 'locations/add_venue.html', {'form': form, 'formpic':formpic})



def edit_venue(request, venue_id):
    venue = models.Venue.objects.get(pk=venue_id)
    form = forms.venue_form(instance=venue)
    if request.method == 'POST':
        form = forms.venue_form(request.POST, request.FILES, instance=venue)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/locations/%i/' % venue.id)
        else:
            error=True
            return render(request, 'locations/edit_venue.html', {'form': form, 'error':error})
    else:
        return render(request, 'locations/edit_venue.html', {'form': form })

def add_facility(request, venue_id):
    venue = models.Venue.objects.get(pk=venue_id)
    form = forms.add_facility_form()
    formpic= forms.facilitypic_form()
    if request.method == 'POST':
        form = forms.add_facility_form(request.POST)
        formpic= forms.facilitypic_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.venue=venue
            instance.save()
            if formpic.is_valid():
                facility=instance.save()
                instancepic=formpic.save(commit=False)
                instancepic.facility = instance
                instancepic.save()
            return HttpResponseRedirect('/locations/%i/' % instance.venue.id)
        else:
            error=True
            return render(request, 'locations/add_venue.html', {'form': form, 'venue' : venue, 'error':error, 'formpic':formpic})
    else:
        return render(request, 'locations/add_venue.html', {'form': form, 'venue' : venue, 'formpic':formpic})

def edit_facility(request, facility_id):
    facility = models.Facility.objects.get(pk=facility_id)
    form = forms.add_facility_form(instance=facility)
    if request.method == 'POST':
        form = forms.add_facility_form(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            f=form.save()
            return HttpResponseRedirect('/locations/%i/' % facility.venue.id)
        else:
            error=True
            return render(request, 'locations/edit_facility.html', {'form': form, 'facility':facility, 'error':error})
    else:
        return render(request, 'locations/edit_facility.html', {'form': form, 'facility':facility})


def search(request):
    error = False
    if 'suburb' in request.GET:
        suburb = request.GET['suburb']
        sport = request.GET['sport']
        if not suburb:
            error = True
            return render(request, 'locations/search.html', {'error': error})
        else:
            try:
                suburb = int(suburb)
            except:
                ValueError
                suburb= suburb.upper()
                try:
                    suburb=models.Suburb.objects.get(suburb=suburb)
                    post_code = suburb.post_code
                except:
                    ValueError
                    locations = []
                    return render(request, 'locations/search_results.html',{'query':suburb, 'locations':locations} )
            if 'surrounding' in request.GET:
                a=post_code-15
                b=post_code+15
            else:
                a=post_code
                b=post_code
            queryset = models.Venue.objects.filter(Q(facility__sports__name__icontains=sport), Q(suburb__post_code__range=(a, b)))
            venue_list = queryset.order_by('name').distinct()
            venue_piclist = []
            for Venue in venue_list:
                venue_piclist.extend(list(models.Venuepic.objects.filter(venue=Venue.id)))
            return render(request, 'locations/search_results.html',{'query':suburb, 'venue_list':venue_list, 'venue_piclist':venue_piclist} )
    else:
        return render(request, 'locations/search.html', {'error': error})

def add_venuepic(request, venue_id):
    venue = models.Venue.objects.get(pk=venue_id)
    form = forms.venuepic_form()
    current_pics = models.Venuepic.objects.filter(venue=venue)
    if request.method == 'POST':
        form = forms.venuepic_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.venue=venue
            instance.save()
            return HttpResponseRedirect('/locations/%i/' %int(venue_id))
        else:
            form = forms.venuepic_form()
            return render(request, 'locations/add_photos.html', {'form': form, 'place':venue, 'current_pics':current_pics })
    else:
        return render(request, 'locations/add_photos.html', {'form': form, 'place':venue, 'current_pics':current_pics})

def add_facilitypic(request, facility_id):
    facility = models.Facility.objects.get(pk=facility_id)
    venue=facility.venue
    form = forms.facilitypic_form()
    current_pics = models.Facilitypic.objects.filter(facility=facility)
    if request.method == 'POST':
        form = forms.facilitypic_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.facility=facility
            instance.save()
            return HttpResponseRedirect('/locations/%i/' %facility.venue.id)
        else:
            form = forms.facilitypic_form()
            return render(request, 'locations/add_photos.html', {'form': form, 'place':facility, 'venue':venue, 'current_pics':current_pics})
    else:
        return render(request, 'locations/add_photos.html', {'form': form, 'place':facility, 'venue':venue, 'current_pics':current_pics})
