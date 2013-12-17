from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^qwiz/(\d+)/$', 'qwiz.views.view_qwiz', name='view_qwiz'),
    url(r'^qwiz/(\d+)/new_question$', 'qwiz.views.add_question', name='add_question'),
    url(r'^qwiz/new$', 'qwiz.views.new_qwiz', name='new_qwiz'),
    #url(r'^admin/', include(admin.site.urls)),
)
