from django.db import models
from django.urls import reverse
from django.contrib import admin

class Account(models.Model):
    username = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    DOB = models.DateField(auto_now=False, auto_now_add=False, null=True)
    email = models.CharField(max_length=200, null=True)
    profilePic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('account-detail', args=[str(self.id)])

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('activity-detail', args=[str(self.id)])

#class Image(models.Model):
#    image = models.ImageField(upload_to="user_images", height_field=None, width_field=None, max_length=None)

class Group(models.Model):
    #Title
    title = models.CharField(max_length=200)

    #Members
    members = models.ManyToManyField(Account, help_text='Select members of this group')
    def displayMembers(self):
        return ', '.join(member.firstName for member in self.members.all()[:3])
    displayMembers.short_description = 'Members'

    #Description
    description = models.TextField(help_text='Enter a description of for group')
    
    #Current Count
    def curMembers(self):
        return self.members.all().count()
    curMembers.short_description = "Number of members"

    #Ideal Count
    idealCount = models.IntegerField(default=1)

    #Activities
    activities = models.ManyToManyField(Activity, help_text='Select the activities for this group')

    profilePic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    def displayActivities(self):
        return ', '.join(act.name for act in self.activities.all()[:3])
    displayActivities.short_description = 'Activites'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group-detail', args=[str(self.id)])

class Event(models.Model):
    title = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField()
    
    timeCreated = models.DateTimeField(auto_now_add=True, null=True)
    timeOccuring = models.DateTimeField(null=True)
    
    reccuring = models.BooleanField(default=False) 
    
    RECCHOICES = (
        ("D", "Daily"),
        ("BW", "Bi-Weekly"),
        ("W", "Weekly"),
        ("F", "Fortnightly"),
        ("M", "Monthly"),
        ("Q", "Quaterly"),
        ("BY", "Bi-Yearly"),
        ("Y", "Yearly"),
    )
    howOften = models.CharField(max_length=11, choices=RECCHOICES, blank=True, null=True)

    location = models.CharField(max_length=500, null=True)

    activities = models.ManyToManyField(Activity, help_text='Select the activities for this group')
    def displayActivities(self):
        return ', '.join(act.name for act in self.activities.all()[:3])
    displayActivities.short_description = 'Activites'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])