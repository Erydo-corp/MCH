from django.db import models


class Category(models.Model):
    """Категории внутри магазина"""
    name = models.CharField('название категории', max_length=200)
    slug = models.SlugField('ссылка', max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Product(models.Model):
    """Товары магазина"""
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField('название', max_length=200)
    image = models.ImageField('картинка', upload_to='products', blank=True)
    description = models.TextField('описание', blank=True)
    price = models.PositiveSmallIntegerField('цена')
    available = models.BooleanField('доступность', default=True)
    slug = models.SlugField('ссылка', max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
