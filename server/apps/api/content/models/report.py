from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class Report(models.Model):
    """
    Модель отчета
    """

    title = models.CharField(verbose_name=_("Заголовок"), max_length=255)
    file_content = models.FileField(_("Документ"),upload_to="content/reports",
        validators=[
            FileExtensionValidator(
                (
                    "pdf",
                    "doc",
                    "docx",
                )
            )
        ],
        blank=True,
        null=True
    )
    presentation_content = models.FileField(_("Презентация"),upload_to="content/reports",
        validators=[
            FileExtensionValidator(
                (
                    "pdf",
                    "doc",
                    "docx",
                    "pptx",
                )
            )
        ],
        blank=True,
        null=True
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Отчет")
        verbose_name_plural = _("Отчеты")
        ordering = ["id"]



