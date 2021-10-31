from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings
# ... the rest of your URLconf here ...


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
]
# urlpatterns += staticfiles_urlpatterns() #add kiye hai delete maar dena (not good for Production)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # THIS WAS IN TUTORIAL

# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)  # THIS WAS ON STACKOVERFLOW
