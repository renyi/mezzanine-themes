try:
    from mezzanine.conf import settings
except ImportError:
    from django.conf import settings


def mezzanine_themes(request):
    return {
        'FAV_ICON': getattr(settings, "TEMPLATE_FAV_ICON", ""),
        'APPLE_ICON': getattr(settings, "TEMPLATE_APPLE_ICON", ""),
        'USE_CDN': getattr(settings, "TEMPLATE_USE_CDN", False),
        'CDN_JQUERY': getattr(settings, "TEMPLATE_CDN_JQUERY", "//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"),
        'CDN_BOOTSTRAP_CSS': getattr(settings, "TEMPLATE_CDN_BOOTSTRAP_CSS", "//netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap-combined.min.css"),
        'CDN_BOOTSTRAP_JS': getattr(settings, "TEMPLATE_CDN_BOOTSTRAP_JS", "//netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/js/bootstrap.min.js"),
    }
