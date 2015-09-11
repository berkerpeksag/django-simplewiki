from django.contrib import admin

from .models import Document, Revision


class RevisionInline(admin.TabularInline):
    model = Revision
    extra = 1
    readonly_fields = ('rendered',)


class DocumentAdmin(admin.ModelAdmin):
    inlines = [RevisionInline]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_on', 'updated_on')

admin.site.register(Document, DocumentAdmin)
admin.site.register(Revision)
