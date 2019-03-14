from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('perfiles/', include(profiles_patterns)),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    #Paths de Auth
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),
]
