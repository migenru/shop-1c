from django.contrib import admin

from .models import TagArticle, TypeArticle, Article, TermArticle

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
