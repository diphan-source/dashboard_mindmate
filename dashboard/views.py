from django.shortcuts import render

# Create your views here.
def home(request):
    sidebar_menu = [x for x in range(20)]
    return render(request, 'index.html', { 'links': sidebar_menu})
