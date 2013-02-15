from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Warmup1.views.home', name='home'),
    # url(r'^Warmup1/', include('Warmup1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
   # url(r'^users/$', 'users.views.index'),
    url(r'^users$', 'users.views.index'),
    url(r'^users/login$', 'users.views.login'),
    url(r'^users/add$', 'users.views.add'),
    url(r'^TESTAPI/resetFixture$', 'users.views.resetFixture'),
    url(r'^TESTAPI/unitTests$', 'users.views.unitTests'),
)
