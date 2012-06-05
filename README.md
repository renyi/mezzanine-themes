Mezzanine Themes
===
A collection of Django/Mezzanine templates. Each of them are designed to override Mezzanine's default template.

mezzanine_default and mezzanine_mobile are compilation of all the templates from Mezzanine. This will be easier for non-Python and non-Django designers to work with the templates.

Inspired by Pinax themes.

Usage
---
It is recommended to place the themes as high as possible, to make sure all the app templates are overridden.

    INSTALLED_APPS = (
        'mezzanine_themes.my_awesome_theme_child',
        'mezzanine_themes.my_awesome_theme',
        'mezzanine_themes.mezzanine_default',
        ...
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
        - template/
            - includes/

To override mezzanine_default templates, just copy the templates into the theme's `templates` directory.

    template/
        - includes/
        - base.html
        - index.html

To override Django App templates, just copy the templates into the theme's `templates` directory.

    template/
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

You'll notice that there are no *.py files in the themes. I prefer it this way, so it looks less scrary when we assign designers to work on the theme. =)

Release Notes
---
2012-06-05: Updated templates to mezzanine 1.1.
2012-03-08:  First release. Examples coming soon.

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