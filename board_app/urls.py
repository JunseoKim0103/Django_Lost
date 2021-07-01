from django.contrib import admin
from board_app.views import index, post, detail
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
