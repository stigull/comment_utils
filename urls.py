from django.conf.urls.defaults import *

from comment_utils.views import post_comment, no_comment

urlpatterns = patterns('',
    url(r'^post/$', no_comment, name = 'no_comment'),
    url(r'^skra-athugasemd/$', post_comment, name = 'post_comment'),
) 
