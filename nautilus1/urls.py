from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nautilus1.views.home', name='home'),
    # url(r'^nautilus1/', include('nautilus1.foo.urls')),
    
    url(r'^$', 'konkurs.views.index'),
    url(r'^login/$', 'konkurs.views.auth_login'),
    url(r'^logout/$', 'konkurs.views.auth_logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
