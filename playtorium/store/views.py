from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    product_data = ProductMaster.objects.all()
    param = {
        'product_data': product_data
    }
    return render(request, 'store.html', param)