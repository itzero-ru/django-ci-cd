from django.db import models

# Create your models here.

class Articles(models.Model):
    """Таблица со статьям"""
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Статья')
    date = models.DateTimeField(auto_now=True)
    tag = models.CharField('Тег', max_length=20, default='',blank=True)

    def __str__(self):
        """Информация, которая возвращается при выводе самого объекта"""
        return self.title

    def get_absolute_url(self):
        """Редирект на ту же статью после ее удаления, обновления"""
        return f'/news/{self.id}'

    class Meta:
        """Жестко указываем название для таблицы.
        
        Django по-умолчанию пишет во множественном числе и присваевает имя класса
        """
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
       
class Comments(models.Model):
    """Таблица с коментариями к статьям"""
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='comments_articles')
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField('Текст коментария')

    def __str__(self):
        return self.text
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
