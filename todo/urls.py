"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import tasklist.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_user, name='login' ),
    path('signup/',authentication.views.signup_user,name='signup'),
    path('home/',tasklist.views.home_view, name='home'),
    path('createtask/',tasklist.views.task_create,name='task-form'),
    path('edittask/<int:task_id>', tasklist.views.task_change, name='edit-task'),
    path('deletetask/<int:task_id>', tasklist.views.task_delete, name='delete-task'),
    path('logout/', authentication.views.logout_user,name='logout-user'),
]
