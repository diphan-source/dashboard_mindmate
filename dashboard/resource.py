from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from dashboard.utils import sidebar_menu
from ussd.models import Resource

@login_required
def resource_page(request):
    resources = Resource.objects.all()
    return render(request, 'resource.html', {
        'resources': resources,
        'links': sidebar_menu
    })

@login_required
def resource_add(request):
    required_fields = ['name', 'description', 'website']
    missing_fields = []
    if request.method == 'POST':
        for field in required_fields:
            if not request.POST.get(field):
                missing_fields.append(field)

        if len(missing_fields) > 0:
            return render(request, 'resource_add.html', {
                'links': sidebar_menu,
                'error': 'Missing fields: {}'.format(', '.join(missing_fields))
            })

        
        Resource.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            website=request.POST.get('website')
        )
        return HttpResponseRedirect('/resources')
    return render(request, 'resource_add.html', {'links': sidebar_menu})
        

@login_required
def resource_edit(request, resource_id):
    resource = Resource.objects.filter(id=resource_id).first()
    if not resource:
        return HttpResponseRedirect('/resources')
    required_fields = ['name', 'description', 'website']
    missing_fields = []
    if request.method == 'POST':
        for field in required_fields:
            if field not in request.POST or request.POST.get(field) == '':
                missing_fields.append(field)

        if len(missing_fields) > 0:
            return render(request, 'resource_edit.html', {
                'links': sidebar_menu,
                'error': 'Missing fields: {}'.format(', '.join(missing_fields)),
                'resource': resource
            })
        
        resource.name = request.POST.get('name')
        resource.description = request.POST.get('description')
        resource.website = request.POST.get('website')
        resource.save()
        return HttpResponseRedirect('/resources')
    return render(request, 'resource_edit.html', {
        'links': sidebar_menu,
        'resource': resource
    })

@login_required
def resource_delete(request, resource_id):
    resource = Resource.objects.filter(id=resource_id).first()
    if resource:
        resource.delete()
    return HttpResponseRedirect('/resources')