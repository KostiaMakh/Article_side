from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Author, Article, Category, Organization


class PostArticle(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'birthday', 'position', 'organization', ]

    class Meta:
        model = Author
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', ]

    class Meta:
        model = Category
        fields = '__all__'


class OrganizationAdmin(admin.ModelAdmin):
    fields = ['title', 'science_profile', ]

    class Meta:
        model = Organization
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = PostArticle
    fields = ['title', 'category', 'content', 'author']

    class Meta:
        model = Article
        fields = '__all__'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Organization, OrganizationAdmin)
