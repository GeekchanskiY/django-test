from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from applications.urls import urlpatters as app_patterns
from vacancies.urls import urlpatters as vacancies_patterns
from users.urls import urlpatters as users_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applications/', include(app_patterns)),
    path('', include(vacancies_patterns)),
    path('users/', include(users_patterns)),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
