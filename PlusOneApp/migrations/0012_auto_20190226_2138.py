# Generated by Django 2.1.7 on 2019-02-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlusOneApp', '0011_account_emailconfirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='profilePic',
            field=models.ImageField(blank=True, default='static/images/default_group_image.png', upload_to=None),
        ),
    ]