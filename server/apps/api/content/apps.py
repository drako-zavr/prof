from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentConfig(AppConfig):
    """Default app config"""

    name = "apps.api.content"
    verbose_name = _("Content")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
