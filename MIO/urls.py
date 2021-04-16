"""MIO URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users.views import ProfileRegisterView, ProfileLoginView, CourierRegisterView

from categories.views import CategoriesView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/register', ProfileRegisterView.as_view()),
    path('profile/login', ProfileLoginView.as_view()),
    path('courier/register', CourierRegisterView.as_view()),
    path('order/', include('orders.urls')),
    path('order_product/', include('orders.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)