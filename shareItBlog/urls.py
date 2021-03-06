from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( 'accounts/', include( 'allauth.urls' ) ),
    path( '', include( 'pages.urls', namespace='pages' ) ),
    path( '', include( 'blog.urls' ) ),
    path( 'ckeditor/', include( 'ckeditor_uploader.urls' ) ),
] 
# + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
    urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )