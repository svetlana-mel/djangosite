from django.contrib import admin

from .models import Events, Types, Organizers, Groups, Age, Participants

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('value', 'comment')
    list_display_links = ('value', 'comment')
    search_fields = ('value', 'comment')

class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_display_links = ('name', 'date')
    search_fields = ('name', 'date', 'town', 'groups', 'age', 'types', 'organizers')

class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email')
    list_display_links = ('fname', 'lname', 'email')
    search_fields = ('fname', 'lname', 'email', 'groups', 'age', 'types', 'organizers')

admin.site.register(Events, EventsAdmin)
admin.site.register(Participants, ParticipantsAdmin)
admin.site.register(Groups, PropertyAdmin)
admin.site.register(Types, PropertyAdmin)
admin.site.register(Age, PropertyAdmin)
admin.site.register(Organizers, PropertyAdmin)