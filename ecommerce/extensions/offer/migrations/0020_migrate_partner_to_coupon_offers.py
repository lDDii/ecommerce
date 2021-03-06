# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 12:47
from __future__ import unicode_literals

from django.db import migrations


def add_partner_to_conditional_offers(apps, schema_editor):
    ConditionalOffer = apps.get_model("offer", "ConditionalOffer")

    for conditional_offer in ConditionalOffer.objects.filter(date_created__year='2018', date_created__month='09'):
        site_configuration = conditional_offer.site.siteconfiguration if conditional_offer.site else None
        if site_configuration and conditional_offer.partner != site_configuration.partner:
            conditional_offer.partner = site_configuration.partner
            conditional_offer.save()


def reverse_add_partner_to_conditional_offers(apps, schema_editor):
    ConditionalOffer = apps.get_model("offer", "ConditionalOffer")

    for conditional_offer in ConditionalOffer.objects.filter(date_created__year='2018', date_created__month='09'):
        if conditional_offer.partner:
            conditional_offer.partner = None
            conditional_offer.save()


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0019_migrate_partner_to_conditional_offers'),
    ]

    operations = [
        migrations.RunPython(add_partner_to_conditional_offers, reverse_add_partner_to_conditional_offers),
    ]
