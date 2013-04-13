from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'latte.views.home', name='home'),
    # url(r'^latte/', include('latte.foo.urls')),

    #url(r'^/$', include('contest.urls')),
    url(r'^$', 'contest.views.IndexHandler'),
    url(r'^ajax$', 'contest.views.AjaxHandler'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
