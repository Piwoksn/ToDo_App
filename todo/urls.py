
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup),
    path('login/', views.loginn),
    path('todo/', views.todo),
    path('edit/<int:serial_no>', views.edit, name="edit"),
    path('delete/<int:serial_no>', views.delete, name="delete"),
    path('logout', views.logoutt, name='logout'),
]
