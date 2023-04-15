from django.contrib import admin

from .models import Author, Article, Publication


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['name', 'email', 'username', 'date_register']


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    list_display = ['author', 'article', 'date_published']
