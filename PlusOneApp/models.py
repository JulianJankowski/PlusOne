from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PlusOneApp.choices import *

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    DOB = models.DateField(auto_now=False, auto_now_add=False, null=True)
    profilePic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, default="static/images/default_profile_icon.jpg")
    emailConfirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def getUsername(self):
        return self.user.username
    getUsername.short_description = "User"

    def get_absolute_url(self):
        return reverse('account-detail', args=[str(self.getUsername())])

@receiver(post_save, sender=User)
def update_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()
        
class Activity(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('activity-detail', args=[str(self.name)])

#class Image(models.Model):
#    image = models.ImageField(upload_to="user_images", height_field=None, width_field=None, max_length=None)

class Group(models.Model):
    #Title
    title = models.CharField(max_length=200, primary_key=True)

    #Description
    description = models.TextField(help_text='Enter a description of for group')
    
    #Current Count
    def curMembers(self):
        return self.membership_set.all().count()
    curMembers.short_description = "Number of members"

    #Ideal Count
    idealCount = models.IntegerField(default=1)

    #Activities
    activities = models.ManyToManyField(Activity, help_text='Select the activities for this group')

    profilePic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, default="static/images/default_group_image.png")
    def displayActivities(self):
        return ', '.join(act.name for act in self.activities.all()[:3])
    displayActivities.short_description = 'Activites'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group-profile', args=[str(self.title)])

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=MEMBER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.group.title

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    
    timeCreated = models.DateTimeField(auto_now_add=True, null=True)
    timeOccuring = models.DateTimeField(null=True)
    
    reccuring = models.BooleanField(default=False) 
    
    howOften = models.CharField(max_length=11, choices=RECCURING_CHOICES, blank=True, null=True)

    location = models.CharField(max_length=500, null=True)

    activities = models.ManyToManyField(Activity, help_text='Select the activities for this event')
    def displayActivities(self):
        return ', '.join(act.name for act in self.activities.all()[:3])
    displayActivities.short_description = 'Activites'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    timePosted = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(null=True)
    timeUploaded = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=500)