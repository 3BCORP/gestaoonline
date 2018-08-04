"""crudcompleto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""


from django.urls import path
from .views import new_cliente,update_cliente, delete_cliente,new_adress, search_cliente

urlpatterns = [
    path('search/', search_cliente, name='search'),
    path('new_adress/', new_adress, name='new_adress'),
    path('new/', new_cliente, name='new'),
    path('update/<int:id>/', update_cliente, name='update'),
    path('delete/<int:id>/', delete_cliente, name='del'),
]