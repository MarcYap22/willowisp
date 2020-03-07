from django.conf.urls import url
from .views import home_page, cloud_page, jester_page, flowey_page

urlpatterns = [
    url(r'^heroes/$', home_page, name='home_page'),
    url(r'^hero/cloud/$', cloud_page, name='cloud_page'),
    url(r'^hero/jester/$', jester_page, name='jester_page'),
    url(r'^hero/sunflowey/$', flowey_page, name='flowey_page'),
]
