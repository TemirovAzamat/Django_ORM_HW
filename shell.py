from blog.models import *

author1 = Author.objects.create(
    name='Нурсултан Бердиев',
    email='nursultanberdiev@gmail.com',
    username='nursultanberdiev',
    date_register='2021-01-04'
)

author2 = Author.objects.create(
    name='Лю Вероника',
    email='ronilyu@gmail.com',
    username='ronik',
    date_register='2023-03-12'
)

author3 = Author.objects.create(
    name='Токтосунова Чынара',
    email='chynara0409@gmail.com',
    username='chynara',
    date_register='2023-11-21'
)

article1 = Article.objects.create(
    title='Что нужно для разработки мобильных приложений: языки и тренды'
)

article2 = Article.objects.create(
    title='Зачем нужно использовать кроссплатформенную систему'
)

article3 = Article.objects.create(
    title='Сравниваем Java и Python или с чего лучше начать'
)

article4 = Article.objects.create(
    title='Новый ChatGPT-4: в чем его особенность'
)

article5 = Article.objects.create(
    title='История компании Boston Dynamics. Как появлялись их роботы'
)


pub1 = Publication.objects.create(date_published='2022-08-12', author=author1, article=article1)
pub2 = Publication.objects.create(date_published='2021-01-22', author=author1, article=article2)
pub3 = Publication.objects.create(date_published='2023-06-02', author=author1, article=article3)
pub4 = Publication.objects.create(date_published='2018-12-22', author=author2, article=article4)
pub5 = Publication.objects.create(date_published='2020-08-17', author=author3, article=article5)


authors = Author.objects.all()
authors.order_by('date_register')


article_nurs = Article.objects.filter(author=author1)

article_nurs


author_after = Author.objects.filter(date_register__gt='2022-10-10')
author_after


pub = Publication.objects.all()

pub_dict = pub.values('author', 'article')
pub_dict


pub = Publication.objects.filter(author__name__contains='В')
pub
