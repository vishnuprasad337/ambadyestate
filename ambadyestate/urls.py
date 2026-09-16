"""
URL configuration for ambadyestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('blog/', views.blog, name='blog')

Class-based views
    1. Add an import:  from other_app.views import Home

Including another URLconf
    1. Add an import:  from django.urls import include, path
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
    # Admin
    # path("admin/", admin.site.urls),

    # Robots.txt
    path(
        "robots.txt",
        robots_txt,
        name="robots_txt",
    ),

    # Sitemap
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    # Application URLs
    path(
        "",
        include("ambadyestate_app.urls"),
    ),
]


# Media files
# WhiteNoise handles static files, so STATIC_URL is NOT added here.
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)


# Custom 404 page
handler404 = "ambadyestate_app.views.page_404"