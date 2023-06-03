from django.template.loader import get_template

def clear_template_cache():
    get_template('base.html').template.cache.clear()
