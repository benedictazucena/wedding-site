from django.db import models


class Invite(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    urlToken = models.CharField(max_length=100, db_index=True)
    pax = models.PositiveSmallIntegerField(default=1)
    rsvp = models.BooleanField(default=None)
    email = models.EmailField(blank=True, db_index=True)
    mobile = models.CharField(max_length=32, blank=True, db_index=True)
    confirmedCompany = models.BooleanField(default=None)
    vaccinationStatus = models.BooleanField(default=None)
    allergies = models.CharField(blank=True, max_length=200)

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)


    def as_dict(self):
        d = dict()
        d['name'] = self.name
        d['rsvp'] = self.rsvp
        d['email'] = self.email
        d['vaccinationStatus'] = self.vaccinationStatus
        d['mobile'] = self.mobile
        return d
