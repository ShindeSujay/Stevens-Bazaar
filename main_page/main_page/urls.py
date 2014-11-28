from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signin.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'signin.views.login'),
    url(r'^auth$', 'signin.views.auth_view'),
    url(r'^logout/$', 'signin.views.logout'),
    url(r'^loggedin/$', 'signin.views.loggedin'),
    url(r'^invalid_login/$', 'signin.views.invalid_login'),
    url(r'^register/$', 'signin.views.register_user'),
    url(r'^register_success/$', 'signin.views.register_success'),
    url(r'^invalid_email/$', 'signin.views.invalid_email'),
    url(r'^about-us/$', 'signin.views.aboutus'),
    url(r'^FirstTimeUser/$', 'signin.views.firsttime'),
    url(r'^FAQs/$', 'signin.views.FAQs'),
    url(r'^the-team/$', 'signin.views.team'),
    url(r'^Terms/$', 'signin.views.terms'),
    url(r'^post_view/$', 'post.views.post_view'),
    url(r'^posts_view/$', 'post.views.posts_view'),
    url(r'^post_success/$', 'post.views.post_success'),
    url(r'^post_invalid/$', 'post.views.post_invalid'),
    url(r'^adPost/$', 'post.views.adpost'),
    url(r'^search/$', 'post.views.search'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)