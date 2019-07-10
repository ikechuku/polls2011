from django.contrib import admin
from . import models as mymod

admin.site.register(mymod.Agentname)
admin.site.register(mymod.AnnouncedPuResults)
admin.site.register(mymod.Ward)
admin.site.register(mymod.AnnouncedLgaResults)
admin.site.register(mymod.PollingUnit)
admin.site.register(mymod.AnnouncedStateResults)
admin.site.register(mymod.AnnouncedWardResults)
admin.site.register(mymod.Lga)
admin.site.register(mymod.Party)
admin.site.register(mymod.States)
