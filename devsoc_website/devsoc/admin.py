from django.contrib import admin
from .models import *

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('name', 'title')

class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ('name', 'subject', 'viewed', 'status')

admin.site.register(model)
admin.site.register(Team, TeamAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Status)
admin.site.register(NoticeTopic)
admin.site.register(Notice)
admin.site.register(NoticeImage)
admin.site.register(Portfolio)