from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticlesConfig(AppConfig):
    """Default app config"""

    name = "apps.api.articles"
    verbose_name = _("Articles")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
