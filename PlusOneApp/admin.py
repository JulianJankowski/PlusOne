from django.contrib import admin
from PlusOneApp.models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('getUsername', 'DOB', 'profilePic')
=======
    list_display = ['DOB']
>>>>>>> registration

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'displayMembers', 'curMembers', 'idealCount', 'displayActivities', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'timeCreated', 'timeOccuring', 'reccuring', 'howOften', 'location', 'displayActivities')