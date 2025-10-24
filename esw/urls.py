from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('academics/', views.academics, name='academics'),
    path('admission/', views.admission, name='admission'),
    path('contact/', views.contact, name='contact'),
    path('admission-form/', views.admission_form_view, name='admission_form_view'),

    # optional extras for your updates
    path('updates/', views.schupdate_list, name='schupdate_list'),
    path('updates/<int:pk>/', views.schupdate_detail, name='schupdate_detail'),
    path('updates/create/', views.schupdate_create, name='schupdate_create'),
      path('contact/', views.contact_view, name='contact'),
]

