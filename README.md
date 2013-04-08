Mezzanine Themes
===
A collection of Django/Mezzanine templates. Each of them are designed to override Mezzanine's default template.

mezzanine_default and mezzanine_mobile are compilation of all the templates from Mezzanine. This will be easier for non-Python and non-Django designers to work with the templates.

Inspired by Pinax themes.


Usage
---
It is recommended to place the themes as high as possible, to make sure all the app templates are overridden.

    1. Add 'mezzanine_themes' to INSTALLED_APP.

        INSTALLED_APPS = (
            'mezzanine_themes.themes.my_awesome_theme_child',
            'mezzanine_themes.themes.my_awesome_theme',
            'mezzanine_themes',
            ...
        )


    2. Add 'mezzanine_themes.context_processors.theme_settings' to TEMPLATE_CONTEXT_PROCESSORS.
       OPTIONAL: Injects helpful context into templates.

        TEMPLATE_CONTEXT_PROCESSORS = (
            ...
            'mezzanine_themes.theme_settings',
        )


    3. Add urls to urls.py.
       OPTIONAL: To serve robots.txt.

        urlpatterns = patterns("",
            ...
            (r"", include(mezzanine_themes.urls)),
        )


Creating your own theme
---
Quoted from Pinax developers, 'Pinax themes are just simple Django Apps'. Actually, this applies to all Django projects as well.

A typical theme structure would look like this,

    my_awesome_theme/
        - static/
            - img/
            - js/
                - scripts.js
            - css/
                - local.css
        - templates/
            - includes/

To override mezzanine_default templates, just copy the templates into the theme's `templates` directory.

    templates/
        - includes/
        - base.html
        - index.html

To override Django App templates, just copy the templates into the theme's `templates` directory.

    templates/
        - admin/
            - change_form.html
            - change_list.html
        - includes/
        - base.html
        - index.html

This overiding structure also helps to organize static files as you don't need duplicate
javacripts or css scripts to the child templates.

    my_awesome_theme/
        - static/
            - js/

    base_theme/
        - static/
            - js/
                - jquery.min.js

From here, the jquery.min.js library in base_theme will also be available to my_awesome_theme, just remember to include both the themes into INSTALLED_APPS.


Release Notes
---
09-04-2013:
- Revamped project.
- Moved all themes to /themes/.
- Added defaults.py and context_processors.py to customize themes.
- Added /plugins/.
- Removed Mezzanine templates.


11-02-2013:
- Updated default templates to Mezzanine 1.3.0 templates.


25-09-2012:
- Added business theme by Dmitry Falk.


11-09-2012:
- Added html5_boilerplate theme by Renyi Khor.


10-09-2012:
- Updated default templates to Mezzanine 1.2.4 templates.


06-06-2012:
- Added Classic theme by Dmitry Falk.


05-06-2012:
- Updated default templates to Mezzanine 1.1 templates.


08-03-2012:
- First release. Examples coming soon.


Contributors
---
If you have a theme you'd like to share, just send a pull request.

    Renyi Khor (https://github.com/renyi)
    Dmitry Falk (https://github.com/dfalk)


External Links
---
    [1] Django: <https://www.djangoproject.com/>
    [2] Mezzanine: <http://mezzanine.jupo.org/>
    [3] Pinax Project: <http://pinaxproject.com/>
