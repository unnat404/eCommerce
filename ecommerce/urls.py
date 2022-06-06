from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings
# ... the rest of your URLconf here ...

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
# urlpatterns += staticfiles_urlpatterns() #add kiye hai delete maar dena (not good for Production)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # THIS WAS IN TUTORIAL

# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)  # THIS WAS ON STACKOVERFLOW
