from django.db import models


class Category(models.Model):
    """Категории магазина"""
    name = models.CharField('название категории', max_length=200)
    slug = models.SlugField('ссылка', max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Категорию товара"
        verbose_name_plural = "Категории товара"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Product(models.Model):
    """Товары магазина"""
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория товара',
    )
    name = models.CharField('название', max_length=200)
    image = models.ImageField('картинка', upload_to='products', blank=True, null=True)
    description = models.TextField('описание', blank=True, null=True)
    price = models.PositiveSmallIntegerField('цена')
    available = models.BooleanField('доступность', default=True)
    slug = models.SlugField('ссылка', max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
