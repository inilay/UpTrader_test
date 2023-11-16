from django.contrib import admin
from tree_menu.models import MenuTree, MenuTreeNode
# Register your models here.

@admin.register(MenuTree)
class MenuTreeAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuTreeNode)
class MenuTreeNodeAdmin(admin.ModelAdmin):
    exclude = ('slug',)
   