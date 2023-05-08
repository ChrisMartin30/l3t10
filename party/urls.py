from django.urls import path
from . import views


# Will have a home page, a link to schedule, or able to type particular month and year.
urlpatterns = [
    path('', views.home, name="home"),
    path('events/', views.events, name="events"),
    path('add_event/', views.add_event, name="add_event"),
    path('mailing_list/', views.mailing_list, name="mailing_list"),
    path('view_mailing_list', views.view_mailing_list, name="view_mailing_list"),
]
