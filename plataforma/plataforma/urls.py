from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('profiles/', include(profiles_patterns)),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('events.urls')),
    #Paths de Auth
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)