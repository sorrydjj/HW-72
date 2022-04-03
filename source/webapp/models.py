from django.db import models

STATUS_CHOICES = (("new", "Новая"), ("moderated", "Модеринован"))


class Quote(models.Model):
    text = models.TextField(max_length=2000,
                            blank=False,
                            null=False,
                            verbose_name="Текс")
    name = models.CharField(max_length=200,
                            null=True,
                            blank=True,
                            verbose_name="Имя")
    email = models.EmailField(max_length=30,
                              verbose_name="Почтовый адрес")
    rating = models.PositiveIntegerField(default=0,
                                         verbose_name="Рейтинг")
    status = models.CharField(max_length=200,
                              choices=STATUS_CHOICES,
                              verbose_name="Статус",
                              default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "quote"
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"

    def __str__(self):
        return f"{self.status}"
