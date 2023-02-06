from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

# handle crsf token. this view does not require it
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.
from ussd.models import SessionTrack, Resource, Therapist, Psychiatrists, MentalHealthProvider

GO_BACK = "0"

@method_decorator(csrf_exempt, name='dispatch')
class UssdView(View):
    def get(self, request):
        return JsonResponse({'status': 'success , Ussd in production Your MentalHealth Matters'})

    def post(self, request):
        self.request = request
        self.session_id = request.POST.get('sessionId')
        self.service_code = request.POST.get('serviceCode')
        self.phone_number = request.POST.get('phoneNumber')
        self.text = self.go_back(request.POST.get('text'))
        self.response = ""
        return self.get_response()

    def go_back(self, text):
        data = text.split('*')
        while GO_BACK in data:
            first_index = data.index(GO_BACK)
            del data[first_index - 1:first_index + 1]
        return '*'.join(data)

    def get_response(self):
        if self.text == "":
            self.response = self.get_home()
        else:
            self.response = self.get_menu()

        return HttpResponse(self.response, content_type='text/plain')

    def get_home(self):
        response = "CON Welcome to MindMate\n"
        response += "1. Resources\n"
        response += "2. Therapists\n"
        response += "3. Psychiatrists\n"
        response += "4. Mental Health Providers\n"
        response += "5. Exit"

        return response

    def get_menu(self):
        menu_selection = self.text.split('*')[-1]
        session_track = SessionTrack.objects.filter(session_id=self.session_id).first()

        if session_track is None:
            session_track = SessionTrack(session_id=self.session_id, phone_number=self.phone_number, menu_selection=menu_selection)
            session_track.save()
        else:
            session_track.menu_selection = menu_selection
            session_track.save()

        if menu_selection == "1":
            response = self.get_resources()
        elif menu_selection == "2":
            response = self.get_therapists()
        elif menu_selection == "3":
            response = self.get_psychiatrists()
        elif menu_selection == "4":
            response = self.get_mental_health_providers()
        elif menu_selection == "5":
            response = self.get_exit()
        elif menu_selection == GO_BACK:
            response = self.get_home()
        else:
            response = self.get_home()

        return response

    def get_resources(self):
        resources = Resource.objects.all()
        response = "CON Select a resource\n"

        for resource in resources:
            response += f"{resource.id}. {resource.name}\n"

        response += f"{GO_BACK}. Go Back"

        return response

    def get_therapists(self):
        therapists = Therapist.objects.all()
        response = "CON Select a therapist\n"

        for therapist in therapists:
            response += f"{therapist.id}. {therapist.name}\n"

        response += f"{GO_BACK}. Go Back"

        return response


    def get_exit(self):
        response = "END Thank you for using MindMate"

        return response


    def get_psychiatrists(self):
        psychiatrists = Psychiatrists.objects.all()
        response = "CON Select a psychiatrist\n"

        for psychiatrist in psychiatrists:
            response += f"{psychiatrist.id}. {psychiatrist.name}\n"

        response += f"{GO_BACK}. Go Back"

        return response

    def get_mental_health_providers(self):
        mental_health_providers = MentalHealthProvider.objects.all()
        response = "CON Select a mental health provider\n"

        for mental_health_provider in mental_health_providers:
            response += f"{mental_health_provider.id}. {mental_health_provider.name}\n"

        response += f"{GO_BACK}. Go Back"

        return response

    
    def handle_therapist(self):
        therapist = Therapist.objects.filter(id=self.text.split('*')[-1]).first()
        response = "END You can contact the therapist on the following details\n"
        response += f"Name: {therapist.name}\n"
        response += f"Phone Number: {therapist.contact}\n"

        return response
