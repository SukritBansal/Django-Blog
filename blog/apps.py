from django.apps import AppConfig

#BlogConfig here is inherited from AppConfig class
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
