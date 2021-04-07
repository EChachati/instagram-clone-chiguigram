"""
Chiguigram URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # Needed To be able to see images in admin dashboard
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),

                  path('',
                       include(
                           ('posts.urls', 'posts'),
                           namespace='posts')
                       ),

                  path('users/',
                       include(
                           ('users.urls', 'users'),
                           namespace='users')
                       ),

              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

# Toma la ruta del archivo multimedia y hace que no lo tome como una ruta de url sino para llegar y abrir el archivo
