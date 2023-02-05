from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from ussd.models import Psychiatrists
from dashboard.utils import sidebar_menu


@login_required
def psychiatrist_page(request):
    psychiatrists = Psychiatrists.objects.all()
    return render(request, 'psychiatrist.html', {'links': sidebar_menu, 'psychiatrists': psychiatrists})


@login_required
def add_psychiatrist(request):
    required_fields = ['first_name', 'last_name', 'contact', 'specialization', 'organization', 'gender']
    missing_fields = []
    if request.method == 'POST':
        for field in required_fields:
            if not request.POST.get(field):
                missing_fields.append(field)

        if len(missing_fields) > 0:
            return render(request, 'add_psychiatrist.html', {'links': sidebar_menu, 'error': 'Missing fields: ' + ', '.join(missing_fields)})
                
        Psychiatrists.objects.create(
            name=request.POST['first_name'] + ' ' + request.POST['last_name'],
            contact=request.POST['contact'],
            specialization=request.POST['specialization'],
            organization=request.POST['organization'],
            gender=request.POST['gender']
        )
        return HttpResponseRedirect('/psychiatrists')
    return render(request, 'add_psychiatrist.html', {'links': sidebar_menu})


@login_required
def edit_psychiatrist(request, psychiatrist_id):
    required_fields = ['first_name', 'last_name', 'contact', 'specialization', 'organization', 'gender']
    missing_fields = []
    psychiatrist = Psychiatrists.objects.filter(id=psychiatrist_id).first()

    if not psychiatrist:
        return HttpResponseRedirect('/psychiatrists')

    psychiatrist.first_name = psychiatrist.name.split(' ')[0]
    psychiatrist.last_name = psychiatrist.name.split(' ')[1]
    if request.method == 'POST':
        for field in required_fields:
            if not request.POST.get(field) or request.POST.get(field) == '':
                missing_fields.append(field)

        if len(missing_fields) > 0:
            return render(request, 'edit_psychiatrist.html', {'links': sidebar_menu, 'error': 'Missing fields: ' + ', '.join(missing_fields), 'psychiatrist': psychiatrist})

        psychiatrist = Psychiatrists.objects.filter(id=psychiatrist_id).first()
        psychiatrist.name = request.POST['first_name'] + ' ' + request.POST['last_name']
        psychiatrist.contact = request.POST['contact']
        psychiatrist.specialization = request.POST['specialization']
        psychiatrist.organization = request.POST['organization']
        psychiatrist.gender = request.POST['gender']
        psychiatrist.save()
        return HttpResponseRedirect('/psychiatrists')
    return render(request, 'edit_psychiatrist.html', {'links': sidebar_menu, 'psychiatrist': psychiatrist})


@login_required
def delete_psychiatrist(request, psychiatrist_id):
    psychiatrist = Psychiatrists.objects.filter(id=psychiatrist_id).first()
    if psychiatrist:
        psychiatrist.delete()
    return HttpResponseRedirect('/psychiatrists')

