# Generated by Django 3.0.7 on 2020-07-03 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='activate',
            new_name='active',
        ),
    ]
