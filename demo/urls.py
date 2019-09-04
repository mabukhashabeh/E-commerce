from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import views
from django.conf.urls import handler404,handler403, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('sooq/', include('core.urls', namespace='core')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
<<<<<<< Updated upstream
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
=======
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

# handler404 = views.error_404
# handler500 = views.error_500
>>>>>>> Stashed changes
