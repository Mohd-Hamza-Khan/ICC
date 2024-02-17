from django.urls import path
from . import views

urlpatterns = [
    path("",views.all_entries, name = 'index'),
    # path("all_entries", views.all_entries, name = "all_entries"),
    path("add_entry", views.add_entry, name = "add_entry"),
    path("delet/<int:id>", views.delet, name = "exit"),
    path("select", views.filter, name = "select"),
    
]