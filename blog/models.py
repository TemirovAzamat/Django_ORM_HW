from django.db import models as m


class AbstractUser(m.Model):
    name = m.CharField(max_length=30, verbose_name='Имя')
    email = m.EmailField(max_length=55, unique=True, verbose_name='Email')

    class Meta:
        abstract = True


class Author(AbstractUser):
    username = m.CharField(max_length=30, verbose_name='Никнейм')
    date_register = m.DateField()

    def __str__(self):
        return self.name


class Article(m.Model):
    title = m.CharField(max_length=255, verbose_name='Заголовок статьи')
    authors = m.ManyToManyField(Author, related_name='articles', through='Publication')

    def __str__(self):
        return self.title


class Publication(m.Model):
    date_published = m.DateField(auto_now=True, verbose_name='Дата публикации')
    author = m.ForeignKey(Author, on_delete=m.CASCADE)
    article = m.ForeignKey(Article, on_delete=m.CASCADE)

    def __str__(self):
        return self.author.name
