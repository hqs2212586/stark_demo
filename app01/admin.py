from django.contrib import admin

# Register your models here.
from .models import Book


class BookConfig(admin.ModelAdmin):
    list_display = ["title", "price"]

    def patch_init(self, request, queryset):
        print("queryset", queryset)
        # queryset <QuerySet [<Book: java>, <Book: python葵花宝典>]>
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"

    actions = [patch_init]


admin.site.register(Book, BookConfig)
