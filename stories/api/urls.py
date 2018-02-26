from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'^stories/$', snippet_list),
    url(r'^stories/([^\s]+)/$', snippet_detail),
    url(r'^entry/$', entry), 
]
