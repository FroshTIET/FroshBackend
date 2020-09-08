from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from landingPage.views import homeView
from rest_framework.authtoken import views

urlpatterns = [
    path("", include("landingPage.urls")),
    path("admin/", admin.site.urls),  # The admin route
    path("api/", include("user_management.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("app/", include("notifications.urls")),
    path("api-token-auth/", views.obtain_auth_token),
]


if settings.DEBUG:
    # Add urls for the debug toolbar
    import debug_toolbar

    urlpatterns += [path("__debug__", include(debug_toolbar.urls))]

    # Static and media serving
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
