from django import template
from tree_menu.models import MenuTree, MenuTreeNode
from django.db.models import F


register = template.Library()

@register.inclusion_tag('tree_menu/tree_menu.html')
def draw_menu(menu_name):
    menu_nodes = MenuTreeNode.objects.filter(menu__menu_name=menu_name).values('node_name', 'slug').annotate(parent=F('parent_node__node_name'))
    grouped_levels = {}
    for i in menu_nodes:
        if i['parent'] not in grouped_levels:
            grouped_levels[i['parent']] = []
        grouped_levels[i['parent']].append(i)
    return {'grouped_levels': grouped_levels, 'menu_title': menu_name}
