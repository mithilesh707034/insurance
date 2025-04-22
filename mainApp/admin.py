from django.contrib import admin
from .models import *

admin.site.register((Contact,Enquiry,Partners,Newsletter,Gallery,Testimonial))
