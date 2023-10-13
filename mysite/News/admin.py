from django.contrib import admin
from .models import News, Category

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'updated_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at', 'category', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
