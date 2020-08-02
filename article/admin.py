from django.contrib import admin

from .models import TagArticle, TypeArticle, Article, TermArticle, Comment

# Register your models here.


admin.site.register(TypeArticle)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(TagArticle)
class TagArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(TermArticle)
class TermArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created', 'is_active')
    list_filter = ('is_active', 'created', 'update')
    search_fields = ('name', 'email', 'content')