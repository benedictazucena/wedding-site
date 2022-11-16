from django.db import models


class Invite(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    urlToken = models.CharField(max_length=100, db_index=True, unique=True)
    pax = models.PositiveSmallIntegerField(default=1)
    isEntourage = models.PositiveSmallIntegerField(default=0)
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
        d['urlToken'] = self.urlToken
        d['confirmedCompany'] = self.confirmedCompany
        d['email'] = self.email
        d['isEntourage'] = self.isEntourage
        d['pax'] = self.pax
        d['mobile'] = self.mobile
        return d
