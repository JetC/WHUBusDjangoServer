from django.conf.urls import *
from views import hello

urlpatterns = patterns('',
    ('^hello/$',hello),
)