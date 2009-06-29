from django.conf.urls.defaults import *
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import admin
from fixmystreet.feeds import LatestReports, LatestReportsByCity, LatestReportsByWard, LatestUpdatesByReport

feeds = {
    'reports': LatestReports,
    'wards': LatestReportsByWard,
    'cities': LatestReportsByCity,
    'report_updates': LatestUpdatesByReport,
}

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^i18n/', include('django.conf.urls.i18n')),
)


urlpatterns += patterns('fixmystreet.views.main',
    (r'^$', 'index'),
    (r'^search', 'search_address'),
    (r'about/$', 'about')
)

urlpatterns += patterns('fixmystreet.views.faq',
    (r'^about/(\S+)$', 'show'),
)


urlpatterns += patterns('fixmystreet.views.promotion',
    (r'^promotions/(\w+)$', 'show'),
)


urlpatterns += patterns('fixmystreet.views.wards',
    (r'^wards/(\d+)', 'show'),       
    (r'^cities/(\d+)/wards/(\d+)', 'show_by_number'),       
    
)

urlpatterns += patterns('fixmystreet.views.cities',
    (r'^cities/(\d+)$', 'show'),       
    (r'^cities', 'index'),
)

urlpatterns += patterns( 'fixmystreet.views.reports.updates',
    (r'^reports/updates/confirm/(\S+)', 'confirm'), 
    (r'^reports/updates/create/', 'create'), 
    (r'^reports/(\d+)/updates/', 'new'),
)


urlpatterns += patterns( 'fixmystreet.views.reports.subscribers',
    (r'^reports/subscribers/confirm/(\S+)', 'confirm'), 
    (r'^reports/subscribers/unsubscribe/(\S+)', 'unsubscribe'),
    (r'^reports/subscribers/create/', 'create'),
    (r'^reports/(\d+)/subscribers/', 'new'),
)

urlpatterns += patterns( 'fixmystreet.views.reports.flags',
    (r'^reports/(\d+)/flags/thanks', 'thanks'),
    (r'^reports/(\d+)/flags', 'new'),
)

urlpatterns += patterns('fixmystreet.views.reports.main',
    (r'^reports/(\d+)$', 'show'),       
    (r'^reports/', 'new'),
)

urlpatterns += patterns('fixmystreet.views.contact',
    (r'^contact/thanks', 'thanks'),
    (r'^contact', 'new'),
)

urlpatterns += patterns('fixmystreet.views.ajax',
    (r'^ajax/categories/(\d+)', 'category_desc'),
)

#The following is used to serve up local media files like images
if settings.LOCAL_DEV:
    baseurlregex = r'^media/(?P<path>.*)$'
    urlpatterns += patterns('',
        (baseurlregex, 'django.views.static.serve',
        {'document_root':  settings.MEDIA_ROOT}),
    )
