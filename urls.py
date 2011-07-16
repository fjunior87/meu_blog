from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
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
	url(r'^contato/$','views.contato'),
	url(r'^comments/',include('django.contrib.comments.urls')),
    # Examples:
    # url(r'^$', 'meu_blog.views.home', name='home'),
    # url(r'^meu_blog/', include('meu_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
<<<<<<< HEAD

if settings.LOCAL:
	urlpatterns += patterns('',
		url(r'^media/(.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT})
	)
=======
#testing
>>>>>>> 549c0119c8171432f69e59c33385b14819945ea1
