from django.contrib import admin

from .models import Document, Revision


class RevisionInline(admin.StackedInline):
    model = Revision
    readonly_fields = ['creator', 'content']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_on', 'updated_on']
    inlines = [RevisionInline]
