from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from ussd.models import MentalHealthProvider
from dashboard.utils import sidebar_menu


@login_required
def mental_health_provider_page(request):
    mh_providers = MentalHealthProvider.objects.all()
    return render(request, 'mh_provider.html', {'links': sidebar_menu, 'mh_providers': mh_providers})


@login_required
def add_provider(request):
    required_fields=['name','contact','field','website' ]
    missing_fields = []
    if request.method == 'POST':
        for field in required_fields:
            if not request.POST.get(field):
                missing_fields.append(field)
                
        if missing_fields:
            return render(request, 'add_provider.html', {'links': sidebar_menu, 'error':  'The following fields are required: {}'.format(', '.join(missing_fields))})
        
        
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        field = request.POST.get('field')
        website = request.POST.get('website')
        
        existing = MentalHealthProvider.objects.filter(name=name)
        if existing:
            return render(request, 'add_provider.html', {'links': sidebar_menu, 'error': 'Provider already exists'})

        # Create a new provider
        MentalHealthProvider.objects.create(
            name=name,
            contact=contact,
            fields=field,
            website=website
        )
        
        return HttpResponseRedirect('/providers')
    
    return render(request, 'add_provider.html', {'links': sidebar_menu})
    
@login_required
def edit_provider(request, provider_id):
    details = MentalHealthProvider.objects.filter(id=provider_id).first()
    if not details:
        return render(request, 'edit_provider.html', {'links': sidebar_menu, 'error': 'Provider does not exist'})
        
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        field = request.POST.get('field')
        website = request.POST.get('website')
            
        details.name = name
        details.contact = contact
        details.field = field
        details.website = website
            
        details.save()
            
        return HttpResponseRedirect('/providers')
    else:
        return render(request, 'edit_provider.html', {'links': sidebar_menu, 'details': details})
    
    
@login_required
def delete_provider(provider_id):
    details = MentalHealthProvider.objects.filter(id=provider_id).first()
    if details:
        details.delete()
    return HttpResponseRedirect('/providers')



