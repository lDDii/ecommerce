# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from oscar.core.loading import get_model

ProductClass = get_model("catalogue", "ProductClass")

WRONG_SLUG = 'enrollment-code'
RIGHT_SLUG = 'enrollment_code'


def fix_enrollment_code_slug(apps, schema_editor):
    """Update the faulty product class."""
    try:
        product_class = ProductClass.objects.get(slug=WRONG_SLUG)
        product_class.slug = RIGHT_SLUG
        product_class.save_without_historical_record()
    except ProductClass.DoesNotExist:
        pass


def revert_migration(apps, schema_editor):
    try:
        ProductClass.skip_history_when_saving = True
        product_class = ProductClass.objects.get(slug=RIGHT_SLUG)
        product_class.slug = WRONG_SLUG
        product_class.save()
    except ProductClass.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
        ('catalogue', '0023_auto_20170215_2234')
    ]
    operations = [
        migrations.RunPython(fix_enrollment_code_slug, revert_migration)
    ]
