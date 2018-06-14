from django.db import models
from tinymce.models import HTMLField


class PricesFork(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    price = models.IntegerField(default=0, verbose_name=u'Цена')
    img = models.ImageField(upload_to='static/img/block6', blank=True, null=True, default=None,
                                  verbose_name=u"Фоновая картинка")
    time = models.FloatField(default=0, verbose_name=u'Длительность ремонта на 1м2 (дней)')
    content = HTMLField(default=None, verbose_name=u"Контент на детальной странице")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Тип ремонта'
        verbose_name_plural = 'Типы ремонтов'


class PlaceType(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Тип помещения")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений в калькуляторе'


class ServicesCategories(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    content = HTMLField(default=None, verbose_name=u"Контент на детальной странице")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Вид работ'
        verbose_name_plural = 'Виды работ'


class ServicesSubcategories(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    content = HTMLField(default=None, verbose_name=u"Контент на детальной странице")
    cateory = models.ForeignKey(ServicesCategories, blank=True, null=True, default=None, on_delete=models.CASCADE)
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'



class Services(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Название")
    price = models.IntegerField(default=0, verbose_name=u'Цена')
    v = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Единицы измерения (м2)")
    content = HTMLField(default=None, verbose_name=u"Контент на детальной странице")
    categorie = models.ForeignKey(ServicesSubcategories, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/block6', blank=True, null=True, default=None,
                                  verbose_name=u"Фоновая картинка")
    slug = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"URL страницы")

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'