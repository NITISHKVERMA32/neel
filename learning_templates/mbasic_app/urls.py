from django.conf.urls import url
from django.urls import path
from mbasic_app import views

# template tagging
app_name = 'mbasic_app'

urlpatterns=[
    path('relative/',views.relative_fun,name='name_relative'),
    path('other/',views.other_fun,name='name_other')
]