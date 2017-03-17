from __future__ import unicode_literals

from django.apps import AppConfig


class BlogConfig(AppConfig):
    list_display = ['first_name', 'id']
    name = 'blog'
