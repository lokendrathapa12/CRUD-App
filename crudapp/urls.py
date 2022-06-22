from django.urls import path
from . import views
urlpatterns = [
    path("",views.HomeView,name='homepage'),
    path("delete/<int:id>/",views.Delete_Data,name='delpage'),
    path("<int:id>/",views.Update_Data,name='updatepage'),
]