"""charoit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('panel/base.html/', include('panel/base.html.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

# sys.path.append('/.../charoit/users')
from users import views as user_view


# TODO: admin - yes; null - NO; register - YES, login - YES, media - YES
urlpatterns = [
    path('', include('panel.urls')),
    path('admin/', admin.site.urls),
    path("register/", user_view.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", user_view.logouting, name='logout'),
    url(r"^content/(?P<path>.*)", serve, {'document_root': settings.MEDIA_ROOT}),
]
