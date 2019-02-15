from django.db import models
from django.urls import reverse
from django.contrib import admin

class Account(models.Model):
    username = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('account-detail', args=[str(self.id)])

class Activity(models.Model)

class Group(models.Model):
    title = models.CharField(max_length=200)
    
    #Creator of the ad
    #host = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    #Members
    members = models.ManyToManyField(Account, help_text='Select members of this group')
    def displayMembers(self):
        return ', '.join(member.firstName for member in self.members.all()[:3])

    displayMembers.short_description = 'Members'


    description = models.TextField(help_text='Enter a description of for group')
    currentCount = models.IntegerField()
    idealCount = models.IntegerField()

    activities = models.ManyToManyField('Activities', help_text='Select the activities for this group')
    def displayActivities(self):
        return ', '.join(act.)

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.id)])