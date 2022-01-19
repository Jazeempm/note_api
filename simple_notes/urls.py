"""simple_notes URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from my_api.views import CreateUserView, NotesViewSet, DeleteImageView, ImageUploadView, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',CreateUserView.as_view() ,name="register"),
    path("delete_image/<int:id>/",DeleteImageView.as_view(),name="deleteimage"),
    path("upload_image/<int:id>/",ImageUploadView.as_view(),name="upload_image"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
