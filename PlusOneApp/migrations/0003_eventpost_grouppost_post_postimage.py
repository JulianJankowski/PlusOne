# Generated by Django 2.2.1 on 2019-05-20 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlusOneApp', '0002_auto_20190519_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timePosted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlusOneApp.Account')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(null=True)),
                ('timeUploaded', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=500)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlusOneApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PlusOneApp.Post')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlusOneApp.Group')),
            ],
            bases=('PlusOneApp.post',),
        ),
        migrations.CreateModel(
            name='EventPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PlusOneApp.Post')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlusOneApp.Event')),
            ],
            bases=('PlusOneApp.post',),
        ),
    ]
