from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

# handle crsf token. this view does not require it
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import africastalking

# Create your views here.
from ussd.models import SessionTrack, Resource, Therapist, Psychiatrists, MentalHealthProvider
from ussd.sms import send_sms
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
        session_track = SessionTrack.objects.filter(session_id=self.session_id).first()

        if session_track is None:
            session_track = SessionTrack(session_id=self.session_id, phone_number=self.phone_number, menu_selection=self.text, flag=0)
            session_track.save()
        else:
            session_track.menu_selection = self.text
            session_track.flag = 0
            session_track.save()

        if self.text == "":
            self.response = self.get_home()
        elif self.text == "1":
            self.response = self.get_resources()
        elif self.text == "2":
            self.response = self.get_therapists()
        elif self.text == "3":
            self.response = self.get_psychiatrists()
        elif self.text == "4":
            self.response = self.get_mental_health_providers()
        elif self.text == "5":
            self.response = self.get_exit()
        elif self.text == "1*1":
            self.response = self.handle_resource()
        elif self.text == "1*2":
            self.response = self.handle_resource_2()
        elif self.text == "1*3":
            self.response = self.handle_resource_3()
        elif self.text == "2*1":
            self.response = self.handle_therapist()
        elif self.text == "2*2":
            self.response = self.handle_therapist_2()
        elif self.text == "2*3":
            self.response = self.handle_therapist_3()
        elif self.text == "3*1":
            self.response = self.handle_psychiatrist()
        elif self.text == "3*2":
            self.response = self.handle_psychiatrist_2()
        elif self.text == "4*1":
            self.response = self.handle_mental_health_provider()
        elif self.text == "4*2":
            self.response = self.handle_mental_health_provider_2()
        elif self.text == "4*3":
            self.response = self.handle_mental_health_provider_3()
        else:
            self.response = self.get_home()
        
        

        return HttpResponse(self.response, content_type='text/plain')

    def get_home(self):
        response = "CON Welcome to MindMate\n"
        response += "1. Resources\n"
        response += "2. Therapists\n"
        response += "3. Psychiatrists\n"
        response += "4. Mental Health Providers\n"
        response += "5. Exit"

        return response


    def get_resources(self ,text= "", flag = 0):
        resources = Resource.objects.all()
        response = "CON Select a resource\n"
        response += "1. Mental Health Management Tips\n"
        response += "2. Hotlines\n"
        response += "3. online Resources\n"
        response += f"{GO_BACK}. Back\n"
        
        if text == '1':
            for resource in resources:
                response = "END Mental Health Management Tips\n"
                response += f"{resource.id}. {resource.description}\n"
                send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        
        elif text == '2':
            for resource in resources:
                response = "END Hotlines\n"
                response += f"{resource.id}. {resource.description}\n"
                send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
            
        elif text == '3':
            for resource in resources:
                response = "END Online Resources\n"
                response += f"{resource.id}. {resource.description}\n"
                send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        else:
            
            return response
    


    def get_therapists(self ,text= "" , flag = 2):
        therapists = Therapist.objects.all()
        response = "CON Select a therapist\n"
        response += "1. Counselling\n"
        response += "2. Psychotherapy\n"
        response += "3. Art Therapy\n"
        response += f"{GO_BACK}. Back\n"
        
        
        if text == '1':
            for therapist in therapists:
                response = "END Counselling\n"
                response += f"{therapist.id}. {therapist.name} + : + {therapist.contact}\n"
                send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        elif text == '2':
            for therapist in therapists:
                response = "END Psychotherapy\n"
                response += f"{therapist.id}. {therapist.name} + : + {therapist.contact}\n"
                send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        elif text == '3':
            for therapist in therapists:
                response = "END Art Therapy\n"
                response += f"{therapist.id}. {therapist.name} + : + {therapist.contact}\n"
                send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        else :
            return response
        # for therapist in therapists:
        #     response += f"{therapist.id}. {therapist.name}\n"

        # response += f"{GO_BACK}. Go Back"

        # return response


    def get_exit(self):
        response = "END Thank you for using MindMate"

        return response


    def get_psychiatrists(self , text="" , flag = 2):
        psychiatrists = Psychiatrists.objects.all()
        response = "CON Select a psychiatrist\n"
        response += "1. Male \n"
        response += "2. Female \n"
        response += f"{GO_BACK}. Back\n"
        
        if text == "1":
            for psychiatrist in psychiatrists:
                response = "END Male psychiatrist\n"
                if psychiatrist.id == 1:
                    response += f"{psychiatrist.name} + : + {psychiatrist.contact}\n"
                    send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        elif text == "2":
            response = "END Female psychiatrist \n"
            for psychiatrist in psychiatrists:
                if psychiatrist.id == 2:
                    response += f"{psychiatrist.name} + : + {psychiatrist.contact}\n"
                    send_sms("Hello, Thank you for using MindMate and we are here for you {response}", self.phone_number)
            return response
        else :
            return response
        # for psychiatrist in psychiatrists:
        #     response += f"{psychiatrist.id}. {psychiatrist.name}\n"

        # response += f"{GO_BACK}. Go Back"

        # return response

    def get_mental_health_providers(self):
        mental_health_providers = MentalHealthProvider.objects.all()
        response = "CON Select a mental health provider\n"
        response += "1. Counselling\n"
        response += "2. Treatment\n"
        response += "3. Support\n"
        response += f"{GO_BACK}. Back\n"

        for mental_health_provider in mental_health_providers:
            response += f"{mental_health_provider.id}. {mental_health_provider.name}\n"

        # response += f"{GO_BACK}. Go Back"

        return response
    
    def handle_mental_health_provider(self):
        mentalprovider = MentalHealthProvider.objects.filter(id=self.text.split('*')[-1]).first()
        if mentalprovider is None:
            return "END Sorry, we could not find the mental health provider you are looking for"
        send_sms("Hello, Thank you for using MindMate and we are here for you {mentalprovider.name} \n {mentalprovider.contact}", self.phone_number)
        response = "END You can contact the mental health provider for counselling on the following details\n"
        response += f"Name: {mentalprovider.name}\n"
        response += f"Phone Number: {mentalprovider.contact}\n"
        response += f"here for you !!\n "
        
        return response
    
    def handle_mental_health_provider_2(self):
        mentalprovider = MentalHealthProvider.objects.filter(id=self.text.split('*')[-1]).first()
        if mentalprovider is None:
            return "END Sorry, we could not find the mental health provider you are looking for"
        
        send_sms("Hello, Thank you for using MindMate and we are here for you {mentalprovider.name} \n {mentalprovider.contact} \n {mentalprovider.field}", self.phone_number)
        response = "END You can contact the mental health provider for treatment on the following details\n"
        response += f"Name: {mentalprovider.name}\n"
        response += f"Phone Number: {mentalprovider.contact}\n"
        response += f"website : {mentalprovider.website}\n"
        
        return response
    
    def handle_mental_health_provider_3(self):
        mentalprovider = MentalHealthProvider.objects.filter(id=self.text.split('*')[-1]).first()
        if mentalprovider is None:
            return "END Sorry, we could not find the mental health provider you are looking for"
        
        send_sms("Hello, Thank you for using MindMate and we are here for you {mentalprovider.name} \n {mentalprovider.contact} \n {mentalprovider.field}", self.phone_number)
        response = "END You can contact the mental health provider for support on the following details\n"
        response += f"Name: {mentalprovider.name}\n"
        response += f"Phone Number: {mentalprovider.contact}\n"
        response += f"website : {mentalprovider.website}\n"
        response += f"here for you !!\n "
        
        return response
        

    
    def handle_therapist(self):
        therapist = Therapist.objects.filter(id=self.text.split('*')[-1]).first()
        if therapist is None:
            return "END Sorry, we could not find the therapist you are looking for"
        
        send_sms("Hello, Thank you for using MindMate and we are here for you {therapist.name} \n {therapist.contact}", self.phone_number)
        response = "END You can contact the therapist on the following details for Counselling\n"
        response += f"Name: {therapist.name}\n"
        response += f"Phone Number: {therapist.contact}\n"

        return 
    
    def handle_therapist_2(self):
        therapist = Therapist.objects.filter(id=self.text.split('*')[-1]).first()
        if therapist is None:
            return "END Sorry, we could not find the therapist you are looking for"
        
        send_sms("Hello, Thank you for using MindMate and we are here for you {therapist.name} \n {therapist.contact}", self.phone_number)
        response = "END You can contact the therapy on the following details for Psychotherapy\n"
        response += f"Name: {therapist.name}\n"
        response += f"Phone Number: {therapist.contact}\n"
        response += f"you are not alone: your mental health matters\n"
        
        return response
    
    def handle_therapist_3(self):
        therapist = Therapist.objects.filter(id=self.text.split('*')[-1]).first()
        if therapist is None:
            return "END Sorry, we could not find the therapist you are looking for"
        
        send_sms("Hello, Thank you for using MindMate and we are here for you {therapist.name} \n {therapist.contact}", self.phone_number)
        response = "END You can contact the therapist on the following details for Art Therapy\n"
        response += f"Name: {therapist.name}\n"
        response += f"Phone Number: {therapist.contact}\n"
        response += f"you are not alone: Art therapy heals and helps in recovery\n"
    
    def handle_psychiatrist(self):
        psychiatrist = Psychiatrists.objects.filter(id=self.text.split('*')[-1]).first()
        if psychiatrist is None:
            return "END Sorry, we could not find the psychiatrist you are looking for"
        
        send_sms(f"Hello, Thank you for using MindMate and we are here for you {psychiatrist.name}", self.phone_number) 
        response = "END You can contact the psychiatrist on the following details\n"
        response += f"Name: {psychiatrist.name}\n"
        response += f"Phone Number: {psychiatrist.contact}\n"

        return response
    
    def handle_psychiatrist_2(self):
        psychiatrist = Psychiatrists.objects.filter(id=self.text.split('*')[-1]).first()
        if psychiatrist is None:
            return "END Sorry, we could not find the psychiatrist you are looking for"
        
        send_sms(f"Hello, Thank you for using MindMate and we are here for you {psychiatrist.name}", self.phone_number)
        response = "END You can contact the psychiatrist on the following details\n"
        response += f"Name: {psychiatrist.name}\n"
        response += f"Phone Number: {psychiatrist.contact}\n"
        response += f"you are not alone: your mental health matters\n"
            
        return response
    
    
    def handle_mental_health_provider(self):
        mental_health_provider = MentalHealthProvider.objects.filter(id=self.text.split('*')[-1]).first()
        if mental_health_provider is None:
            return "END Sorry, we could not find the mental health provider you are looking for"
        
        send_sms(f"Hello, Thank you for using MindMate and we are here for you {mental_health_provider.name}", self.phone_number)
        response = "END You can contact the mental health provider on the following details\n"
        response += f"Name: {mental_health_provider.name}\n"
        response += f"Phone Number: {mental_health_provider.contact}\n"

        return response
    
    def handle_resource(self):
        resource = Resource.objects.filter(id=self.text.split('*')[-1]).first()
        if resource is None:
            return "END Sorry, we could not find the resource you are looking for"

        send_sms(f"Hello, Thank you for using MindMate and we are here for you {resource.description}\n{resource.website}", self.phone_number)
        response = "END You can access the resource on the following details\n"
        response += f"Name: {resource.name}\n"
        response += f"Link: {resource.website}\n"

        return response
    
    def handle_resource_2(self):
        resource = Resource.objects.filter(id=self.text.split("*")[-1]).first()
        if resource is None:
            return "END Sorry , we could not find the resource you are looking for"
        
        send_sms(f"Hello , Thank you for using MindMate and we are here for you {resource.website}", self.phone_number)
        response = "END You can access the resource on the following details\n"
        response += f"Name: {resource.name}\n"
        response += f"Link: {resource.website}\n"
        
        return response
        
    def handle_resource_3(self):
        resource = Resource.objects.filter(id=self.text.split("*")[-1]).first()
        if resource is None:
            return "END Sorry , we could not find the resource you are looking for"
        
        send_sms(f"Hello , Thank you for using MindMate and we are here for you {resource.website}\n {resource.description}", self.phone_number)
        response = "END You can access the resource on the following details\n"
        response += f"Name: {resource.name}\n"
        response += f"Link: {resource.website}\n"
        response += f"Description: {resource.description}\n"

