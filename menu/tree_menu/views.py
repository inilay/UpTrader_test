from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect


class HomePage(View):
    template_name = 'tree_menu/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class NodePage(View):
    template_name = 'tree_menu/node.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'info': f"Content from {self.kwargs['slug']} page"})