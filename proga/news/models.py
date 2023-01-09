from django.db import models

#создем класс для новости
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='') #название новости
    anons = models.CharField('Анонс', max_length=250, default='') #анонс новости
    full_text = models.TextField('Статья') #текст новости
    date = models.DateTimeField('Дата публикации') #дата новости

    def __str__(self):
        #return f'Новость: {self.title}' каким образом будет выводиться каждый отдельный объект
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


