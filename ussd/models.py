from django.db import models


class ExtraMixin(object):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at => only update when the model is updated
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
class SessionTrack(models.Model, ExtraMixin):
    session_id = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)
    menu_selection = models.CharField(max_length=255, null=False)
    flag = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = 'ussd_session_track'

    def __str__(self):
        return self.session_id

class Resource(models.Model, ExtraMixin):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    website = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'ussd_resources'

    def __str__(self):
        return self.name


class Therapist(models.Model, ExtraMixin):
    name = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=255, null=False)
    specialization = models.CharField(max_length=255, null=False)
    organization = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'ussd_therapists'

    def __str__(self):
        return self.name


class Psychiatrists(models.Model, ExtraMixin):
    name = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=255, null=False)
    specialization = models.CharField(max_length=255, null=False)
    organization = models.CharField(max_length=255, null=False)


    class Meta:
        db_table = 'ussd_psychiatrists'

    def __str__(self):
        return self.name


class MentalHealthProvider(models.Model, ExtraMixin):
    name = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=255, null=False)
    fields = models.CharField(max_length=255, null=False)
    website = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'ussd_mental_health_providers'

    def __str__(self):
        return self.name
