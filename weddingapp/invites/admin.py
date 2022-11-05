from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Invite

class InviteAdmin(VersionAdmin):
    list_display = ('id', 'name', 'urlToken', 'pax', 'rsvp', 'confirmedCompany', 'email', 'vaccinationStatus', 'allergies', 'created', 'modified')
    search_fields = ('id', 'urlToken', 'name')
    readonly_fields = ('created', 'modified', )

admin.site.register(Invite, InviteAdmin)