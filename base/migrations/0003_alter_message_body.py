# Generated by Django 4.1.5 on 2023-01-24 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(),
        ),
    ]
