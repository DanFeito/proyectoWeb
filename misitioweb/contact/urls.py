from django.urls import path

from contact import views as contact_view

urlpatterns = [
    path('contact/', contact_view.contact, name="contact"),
]