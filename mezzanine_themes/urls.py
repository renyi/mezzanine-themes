from django.conf.urls.defaults import patterns, include, url

try:
    from django.views.generic.base import TemplateView
    urlpatterns = patterns('',
        url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    )
except:
    urlpatterns = patterns('django.views.generic.simple',
        (r'^robots\.txt$', 'direct_to_template', {'template': 'robots.txt'}),
    )
