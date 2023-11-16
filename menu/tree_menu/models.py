from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class MenuTree(models.Model):
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.menu_name

class MenuTreeNode(models.Model):
    node_name = models.CharField(max_length=50)
    menu = models.ForeignKey('MenuTree', related_name='nodes', on_delete=models.CASCADE)
    parent_node = models.ForeignKey('MenuTreeNode', related_name='children_nodes', on_delete=models.CASCADE, null=True, blank=True, default=None)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.node_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.node_name

    def get_absolute_url(self):
        return reverse("node", kwargs={"slug": self.slug})
