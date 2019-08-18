from app.controllers import homecontroller
from django.conf.urls import url
urlpatterns = [
    url(r'^home/index$', homecontroller.index),
]
