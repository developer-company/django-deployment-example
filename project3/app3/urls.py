from django.conf.urls import url
from app3 import views

urlpatterns=[
  url(r'^$',views.index,name="index"),
]
