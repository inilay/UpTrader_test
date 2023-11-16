from django import template
from tree_menu.models import MenuTree, MenuTreeNode

register = template.Library()

@register.inclusion_tag('tree_menu/tree_level.html')
def draw_menu_level(grouped_levels, current_level):
    return {'grouped_levels': grouped_levels, 'current_level_nodes': grouped_levels[current_level]}