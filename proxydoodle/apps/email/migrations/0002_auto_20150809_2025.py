# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcategory',
            name='can_unsubscribe',
            field=models.BooleanField(default=True, help_text=b'If these emails are transactional, then subscribe/unsubscribe functionality is not needed'),
        ),
        migrations.AddField(
            model_name='emailreceipt',
            name='sending_error',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailreceipt',
            name='sending_error_message',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='emailreceipt',
            name='viewed_from_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailreceipt',
            name='viewed_online',
            field=models.BooleanField(default=False),
        ),
    ]
