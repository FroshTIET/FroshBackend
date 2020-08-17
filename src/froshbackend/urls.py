from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from landingPage.views import homeView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", include("landingPage.urls")),
    path("whodunit/", include("whodunit.urls")),
    path("login/", LoginView.as_view(template_name='user_management/login.html'),name="login" ),
    path('logout/', LogoutView.as_view(template_name='user_management/logout.html'), name='logout'),

    path("admin/", admin.site.urls),  # The admin route
    path("api/", include("user_management.urls")),
    path("api-auth/", include("rest_framework.urls")),
]


if settings.DEBUG:
    # Add urls for the debug toolbar
    import debug_toolbar

    urlpatterns += [path("__debug__", include(debug_toolbar.urls))]

    # Static and media serving
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
