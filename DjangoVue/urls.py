"""DjangoVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from users.urls import router as user_router
from posts.urls import router as post_router
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^api/v1/', include(user_router.urls)),
    url(r'^api/v1/', include(post_router.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^users/$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/v1/auth/', obtain_jwt_token),
    url(r'^api/v1/refresh/', refresh_jwt_token),
    # 静的ファイルのルーティング /static/がきた場合
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 