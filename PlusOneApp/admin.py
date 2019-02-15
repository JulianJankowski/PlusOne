from django.contrib import admin
from PlusOneApp.models import *



admin.site.register(Account)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'displayMembers', 'description')