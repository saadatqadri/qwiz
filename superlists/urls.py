from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'qwiz.views.home_page', name="home"),
    url(r'^qwiz/the-only-qwiz-in-the-world/$', 'qwiz.views.view_qwiz', name='view_qwiz'),
    url(r'^qwiz/new$', 'qwiz.views.new_qwiz', name='new_qwiz'),
    #url(r'^admin/', include(admin.site.urls)),
)
