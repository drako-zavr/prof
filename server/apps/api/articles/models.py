import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    """
    Модель новости
    """

    title = models.CharField(verbose_name=_("Заголовок"), max_length=1023)
    photo = models.ImageField(verbose_name=_("Фотография"), default="zaglushka.jpg", upload_to="content/news") 
    content = models.TextField(verbose_name=_("Содержание"))
    pub_date = models.DateField(verbose_name=_("Дата публикации"),default=datetime.date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
        ordering = ["id"]

class ArticleImage(models.Model):
    """
    Модель изображений новости
    """
    article = models.ForeignKey(Article, verbose_name=_("Новость"), on_delete=models.CASCADE, related_name="images")
    photo = models.ImageField(verbose_name=_("Фотография"), blank=True, upload_to="content/news/gallery")
    order = models.PositiveIntegerField(
        _("Порядок вывода"),
        default=0,
        db_index=True,
    )


    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")
        ordering = ["order"]
