"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('getjson/<id>/',views.getjson,name='getjson'),
    path('getjsonall',views.getjsonall,name='getjsonall'),
    path('listall',views.listall2,name='listall2'),
    re_path(r'^list/(?P<user_id>\w+)/$',views.listall,name="listall"),
    re_path(r'listget/$',views.listget,name='listget'),
]
