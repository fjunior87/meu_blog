from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos
urlpatterns = patterns('',
	url(r'^$', 'django.views.generic.date_based.archive_index',
	{'queryset': Artigo.objects.all(), 'date_field':'publicacao'}),
	url(r'^rss/(?P<url>.*)/$','django.contrib.syndication.views.feed',
	{'feed_dict': {'ultimos': UltimosArtigos}}),
	url(r'^artigo/(?P<artigo_id>\d+)/$','blog.views.artigo'),
	url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'meu_blog.views.home', name='home'),
    # url(r'^meu_blog/', include('meu_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
