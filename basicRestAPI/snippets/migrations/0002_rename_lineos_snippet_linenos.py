# Generated by Django 4.0.1 on 2022-01-20 18:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineos',
            new_name='linenos',
        ),
    ]
