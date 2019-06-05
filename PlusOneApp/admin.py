from django.contrib import admin
from PlusOneApp.models import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['getUsername', 'id', 'DOB']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'curMembers', 'idealCount', 'displayActivities', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'timeCreated', 'timeOccuring', 'reccuring', 'howOften', 'location', 'displayActivities')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'group', 'status')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'timePosted', 'author')