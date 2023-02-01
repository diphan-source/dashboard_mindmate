from django.contrib import admin

# Register your models here.
from ussd.models import SessionTrack, Resource, Therapist, Psychiatrists

admin.site.register(SessionTrack)
admin.site.register(Resource)
admin.site.register(Therapist)
admin.site.register(Psychiatrists)
