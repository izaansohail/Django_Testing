# Generated by Django 3.2.5 on 2021-07-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210706_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='address1',
            field=models.CharField(default=None, max_length=200),
        ),
    ]