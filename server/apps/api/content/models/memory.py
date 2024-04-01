from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class Memory(models.Model):
    """
    Модель памяти
    """

    firstname = models.CharField(verbose_name=_("Имя"), max_length=255)
    lastname = models.CharField(verbose_name=_("Фамилия"), max_length=255, blank=True)
    midname = models.CharField(verbose_name=_("Отчество"), max_length=255, blank=True)
    photo = models.ImageField(verbose_name=_("Фотография"), blank=True,)
    description = models.TextField(verbose_name=_("Описание"))
    file_content = models.FileField(_("Документ"),upload_to="content/documents",
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


    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = _("Память")
        verbose_name_plural = _("Память")
        ordering = ["id"]



