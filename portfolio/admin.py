from django.contrib import admin
from.models import postForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class postAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = postForm
        fields = '__all__'
        
class postAdmin(admin.ModelAdmin):
    form = postAdminForm
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'body')
# Register your models here.
admin.site.register(postForm)