"""
URL configuration for ambadyestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

from ambadyestate_app.sitemaps import (
    StaticViewSitemap,
    RoomSitemap,
    ActivitySitemap,
    NearbyDestinationSitemap,
    PackageSitemap,
    BlogSitemap,
)

sitemaps = {
    "static": StaticViewSitemap,
    "rooms": RoomSitemap,
    "activities": ActivitySitemap,
    "nearby_destinations": NearbyDestinationSitemap,
    "packages": PackageSitemap,
    "blog": BlogSitemap,
}


def robots_txt(request):
    content = """User-agent: *
Disallow: /login/
Disallow: /dashboard/
Disallow: /admin-logout/
Disallow: /blogs/
Disallow: /testimonials/
Disallow: /add-review
Disallow: /categories/
Disallow: /list-images/
Disallow: /add_image/
Disallow: /delete-image/
Disallow: /rooms/
Disallow: /activities/
Disallow: /nearby-destinations/
Disallow: /packages/
Disallow: /reservations/
Disallow: /enquiries/
Disallow: /contact/
Disallow: /media/private/
Allow: /static/
Allow: /

Sitemap: https://ambadyestate.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("robots.txt", robots_txt, name="robots_txt"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('', include('ambadyestate_app.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "ambadyestate_app.views.page_404"