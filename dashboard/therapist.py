from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from dashboard.utils import sidebar_menu


@login_required
def therapist_page(request):
    return render(request, 'therapist.html', {'links': sidebar_menu})