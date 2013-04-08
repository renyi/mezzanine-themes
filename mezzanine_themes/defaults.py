try:
    from mezzanine.conf import register_setting
    from django.utils.translation import ugettext as _

    register_setting(
        name="TEMPLATE_FAV_ICON",
        description=_("FAV_ICON"),
        editable=True,
        default="data:image/x-icon;base64,AAABAAEAEBACAAAAAACwAAAAFgAAACgAAAAQAAAAIAAAAAEAAQAAAAAAQAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAA////AIwBAACCBwAAAeEAAAHBAAA/+QAAI7kAAELtAADBywAAwXkAAMAJAADAsQAA4OMAAGOjAAB+EgAAYA4AAB/8AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA",
    )

    register_setting(
        name="TEMPLATE_APPLE_ICON",
        description=_("APPLE_ICON"),
        editable=True,
        default='',
    )

    register_setting(
        name="TEMPLATE_USE_CDN",
        description=_("USE_CDN"),
        editable=True,
        default=False,
    )

    register_setting(
        name="TEMPLATE_CDN_JQUERY",
        description=_("JQUERY CDN url"),
        editable=True,
        default="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
    )

    register_setting(
        name="TEMPLATE_CDN_BOOTSTRAP_CSS",
        description=_("Bootstrap CDN url (css)"),
        editable=True,
        default="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css",
    )

    register_setting(
        name="TEMPLATE_CDN_BOOTSTRAP_JS",
        description=_("Bootstrap CDN url (js)"),
        editable=True,
        default="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/js/bootstrap.min.js",
    )
except ImportError:
    # You're missing one of Mezzanine's best feature !
    pass
