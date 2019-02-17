from django.contrib import admin
from PlusOneApp.models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstName', 'lastName', 'DOB', 'email')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'timeCreated', 'location', 'timeOccuring', 'reccuring', 'displayMembers', 'curMembers', 'idealCount', 'displayActivities', 'description')