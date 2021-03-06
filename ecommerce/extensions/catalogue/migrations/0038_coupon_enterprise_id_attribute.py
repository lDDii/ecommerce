# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from oscar.core.loading import get_model

from ecommerce.core.constants import COUPON_PRODUCT_CLASS_NAME

ProductAttribute = get_model("catalogue", "ProductAttribute")
ProductClass = get_model("catalogue", "ProductClass")


def create_enterprise_id_attribute(apps, schema_editor):
    """Create coupon enterprise_customer_uuid attribute."""
    coupon = ProductClass.objects.get(name=COUPON_PRODUCT_CLASS_NAME)
    ProductAttribute.objects.create(
        product_class=coupon,
        name='Enterprise Customer UUID',
        code='enterprise_customer_uuid',
        type='text',
        required=False
    )


def remove_enterprise_id_attribute(apps, schema_editor):
    """Remove coupon enterprise_customer_uuid attribute."""
    coupon = ProductClass.objects.get(name=COUPON_PRODUCT_CLASS_NAME)
    ProductAttribute.objects.get(product_class=coupon, code='enterprise_customer_uuid').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0037_add_sec_disc_reward_coupon_category')
    ]
    operations = [
        migrations.RunPython(create_enterprise_id_attribute, remove_enterprise_id_attribute)
    ]
