from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Invite

class InviteAdmin(VersionAdmin):
    list_display = ('id', 'name', 'urlToken', 'isEntourage', 'pax', 'rsvp', 'confirmedPax', 'email', 'vaccinationStatus', 'allergies', 'modified')
    search_fields = ('id', 'urlToken', 'name')
    readonly_fields = ('created', 'modified', )

admin.site.register(Invite, InviteAdmin)