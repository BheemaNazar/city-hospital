from django.urls import path,include
from .import views
from django.conf.urls.static import  static
from django.conf import settings
urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('booking',views.booking,name='booking'),
    path('department',views.department,name='department'),
    path('doctors',views.doctors,name='doctor')
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)