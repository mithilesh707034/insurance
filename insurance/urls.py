from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('enquiry-data/',views.enquiry_data),
    path('newsletter/',views.newsletter),
    path('clear_session/<ops>/',views.clear_session),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
