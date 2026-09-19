"""
URL configuration for ambadyestate project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sites.models import Site
from django.http import HttpResponse, JsonResponse

from ambadyestate_app.sitemaps import (
    StaticViewSitemap,
    RoomSitemap,
    ActivitySitemap,
    NearbyDestinationSitemap,
    PackageSitemap,
    BlogSitemap,
)


# =========================================================
# SITEMAPS
# =========================================================

sitemaps = {
    "static": StaticViewSitemap,
    "rooms": RoomSitemap,
    "activities": ActivitySitemap,
    "nearby_destinations": NearbyDestinationSitemap,
    "packages": PackageSitemap,
    "blog": BlogSitemap,
}


# =========================================================
# ROBOTS.TXT
# =========================================================

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
    return HttpResponse(
        content,
        content_type="text/plain",
    )


# =========================================================
# TEMPORARY SITE FIX
# =========================================================

def fix_site(request):
    """
    One-time URL to create/update the Django Site record
    for the production domain.
    """

    site, created = Site.objects.get_or_create(
        id=1,
        defaults={
            "domain": "ambadyestate.com",
            "name": "Ambady Estate",
        },
    )

    site.domain = "ambadyestate.com"
    site.name = "Ambady Estate"
    site.save()

    if created:
        message = "Django Site created successfully."
    else:
        message = "Django Site updated successfully."

    return HttpResponse(
        f"{message}<br>"
        f"Domain: {site.domain}<br>"
        f"Name: {site.name}"
    )


# =========================================================
# HEALTH CHECK
# =========================================================

def health_check(request):
    return JsonResponse({"status": "ok"})


# =========================================================
# URL PATTERNS
# =========================================================

urlpatterns = [

    # -----------------------------------------------------
    # Robots.txt
    # -----------------------------------------------------
    path(
        "robots.txt",
        robots_txt,
        name="robots_txt",
    ),

    # -----------------------------------------------------
    # Sitemap
    # -----------------------------------------------------
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    # -----------------------------------------------------
    # TEMPORARY: Fix Django Site domain
    # -----------------------------------------------------
    path(
        "fix-site-ambady/",
        fix_site,
        name="fix_site",
    ),

    # -----------------------------------------------------
    # Health check
    # -----------------------------------------------------
    path(
        "h-e-alth/",
        health_check,
        name="health_check",
    ),

    # -----------------------------------------------------
    # Application URLs
    # -----------------------------------------------------
    path(
        "",
        include("ambadyestate_app.urls"),
    ),
]


# =========================================================
# MEDIA FILES
# =========================================================




# =========================================================
# CUSTOM 404 PAGE
# =========================================================

handler404 = "ambadyestate_app.views.page_404"