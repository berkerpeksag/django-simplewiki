from django.contrib import admin

from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_on', 'updated_on')

admin.site.register(Document, DocumentAdmin)
