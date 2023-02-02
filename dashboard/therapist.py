from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from dashboard.utils import sidebar_menu
from ussd.models import Therapist


@login_required
def therapist_page(request):
    therapists = Therapist.objects.all()
    return render(request, 'therapist.html', {'links': sidebar_menu, 'therapists': therapists})


@login_required
def add_therapist(request):
    required_fields = ['first_name', 'last_name', 'contact', 'organization', 'specialization', 'gender']
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        organization = request.POST.get('organization')
        specialization = request.POST.get('specialization')
        gender = request.POST.get('gender')

        name = f"{first_name} {last_name}"

        existing = Therapist.objects.filter(name=name)
        if existing:
            return render(request, 'add_therapist.html', {'links': sidebar_menu, 'error': 'Therapist already exists'})

        # Create a new therapist
        new_therapist = Therapist(
            name=name,
            contact=contact,
            organization=organization,
            specialization=specialization,
            gender=gender
        )
        new_therapist.save()
        
        return HttpResponseRedirect('/therapists')
    else:
        return render(request, 'add_therapist.html', {'links': sidebar_menu})


@login_required
def edit_therapist(request, therapist_id):
    pass


@login_required
def delete_therapist(request, therapist_id):
    pass


@login_required
def therapist_details(request, therapist_id):
    pass