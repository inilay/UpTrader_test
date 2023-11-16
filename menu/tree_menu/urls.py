from django.urls import path, include, re_path
from tree_menu.views import HomePage, NodePage



urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<slug:slug>/', NodePage.as_view(), name='node'),
]