from django.db.models import Q, Subquery
from blog.models import *

# 1
# Добавить СО-автора, надеюсь правильно понял
Publication.objects.create(date_published='2023-08-17', author=author2, article=article1)
Publication.objects.create(date_published='2022-08-17', author=author3, article=article2)


# 2
# Classic
Publication.objects.filter(author__email__icontains='@gmail.com', date_published__lt='2023-04-15')

# Join
Publication.objects.filter(author__email__icontains='@gmail.com') & Publication.objects.filter(
    date_published__lt='2023-04-15'
)

# Q
Publication.objects.filter(Q(author__email__icontains='@gmail.com'), Q(date_published__lt='2023-04-15'))


# 2
# Classic is missing

# Join
Author.objects.filter(name__icontains='Нурсултан Бердиев') | Author.objects.filter(date_register='2021-01-04')

# Q
Author.objects.filter(
    Q(name__icontains='Нурсултан Бердиев') |
    Q(date_register='2021-01-04')
)


# 3
# Exclude
Publication.objects.exclude(author__name__icontains='Вероника')

# Q
Publication.objects.filter(
    ~Q(author__name__icontains='Вероника')
)


# 4
Author.objects.all().only('username')


# 5
# Subquery
Publication.objects.filter(
    author__in=Subquery(
        Author.objects.filter(
            Q(name__icontains='Вероника') |
            Q(name__icontains='Чынара'),
            ~Q(date_register='2021-01-04')
        ).values('id')
    )
)
