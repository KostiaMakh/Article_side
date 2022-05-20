from django.db import models
from pytils.translit import slugify


# Abstract class User
class User(models.Model):
    slug = models.CharField(max_length=250, verbose_name='url')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        abstract = True


# Article
class Article(models.Model):
    slug = models.CharField(max_length=250, verbose_name='url')
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ManyToManyField('author')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(self.title)}'
        super(Article, self).save(*args, **kwargs)

    class Mate:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


# Information about author
class Author(User):
    position = models.CharField(max_length=250)
    organization = models.ForeignKey('organization', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(self.name)}-{slugify(self.surname)}'
        super(Author, self).save(*args, **kwargs)

    class Mate:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


# Blog categories
class Category(models.Model):
    slug = models.CharField(max_length=250, verbose_name='url')
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(self.title)}'
        super(Category, self).save(*args, **kwargs)

    class Mate:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Scientific organization about
class Organization(models.Model):
    slug = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    science_profile = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Organization, self).save(*args, **kwargs)
        self.slug = f'{self.pk}-{slugify(self.title)}'
        super(Organization, self).save(*args, **kwargs)

    class Mate:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'