from stark.service.stark import site, ModelStark
from django.utils.safestring import mark_safe
from django.urls import reverse
from .models import *
from django.forms import ModelForm


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        labels = {
            "title": "书籍名称",
            "publishDate": "出版日期",
            "price": "价格",
            "publish": "出版社",
            "authors": "作者"
        }


class BookConfig(ModelStark):
    list_display = ["title", "price", "publishDate", "publish", "authors"]
    list_display_links = ["title"]
    modelform_class = BookModelForm
    search_fields = ['title', "price"]

    def patch_init(self, request, queryset):
        print(queryset)
        queryset.update(price=123)

    patch_init.short_description = "批量初始化"
    actions = [patch_init]
    list_filter = ["title", "publish", "authors", ]   # 普通字段、一对多、多对多


site.register(Book, BookConfig)


site.register(Publish)
site.register(Author)
site.register(AuthorDetail)

