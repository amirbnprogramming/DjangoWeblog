from django.contrib import admin
from articles.models import Category, Article, Comment

main_list = ['is_active', 'created_at', 'updated_at', ]


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent'] + main_list
    list_editable = ['parent', 'is_active', ]
    list_display_links = ['title', ]
    list_filter = main_list


class CommentAdmin(admin.TabularInline):
    list_display = ['article', 'author', 'text'] + main_list
    list_editable = ['is_active', ]
    list_display_links = ['text', ]
    list_filter = main_list
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['author', 'category', 'title', ] + main_list
    list_editable = ['author', 'category', 'is_active', ]
    list_display_links = ['title', ]
    list_filter = main_list
    inlines = [CommentAdmin]
