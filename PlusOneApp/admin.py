from django.contrib import admin
from PlusOneApp.models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstName', 'lastName')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'displayMembers', 'displayActivities', "currentCount", "idealCount", 'description')