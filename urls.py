from django.conf.urls.defaults import *

from comment_utils.views import post_comment

urlpatterns = patterns('',
    url(r'^skra-athugasemd/$', post_comment, name = 'post_comment'),
) 
