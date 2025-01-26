from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    product_data = ProductMaster.objects.all()
    all_coupons = CouponMaster.objects.all()

    # Filter coupons based on category in Python
    coupon_coupon = all_coupons.filter(coupon_category="Coupon")
    ontop_coupon = all_coupons.filter(coupon_category="On Top")
    seasonal_coupon = all_coupons.filter(coupon_category="Seasonal")
    param = {
        'product_data': product_data,
        'coupon_coupon': coupon_coupon,
        'ontop_coupon': ontop_coupon,
        'seasonal_coupon': seasonal_coupon,
    }
    return render(request, 'store.html', param)