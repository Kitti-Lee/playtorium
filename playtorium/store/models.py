from django.db import models

# Create your models here.
class ProductMaster(models.Model):
    product_id = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    product_description = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image_file = models.CharField(max_length=255, null=True, blank=True)

class CouponMaster(models.Model):
    coupon_id = models.CharField(max_length=255, null=True, blank=True)
    coupon_name = models.CharField(max_length=255, null=True, blank=True)
    coupon_description = models.CharField(max_length=255, null=True, blank=True)
    coupon_type = models.CharField(max_length=255, null=True, blank=True)
    coupon_category = models.CharField(max_length=255, null=True, blank=True)
    discount = models.CharField(max_length=255, null=True, blank=True)
    image_file = models.CharField(max_length=255, null=True, blank=True)
