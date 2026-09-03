from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, Room, Activity, NearbyDestination, Package


class AmbadyEstateSitemap(Sitemap):
    protocol = "https"

    def get_domain(self, site=None):
        return "ambadyestate.com"


# --------- Static Pages ---------
class StaticViewSitemap(AmbadyEstateSitemap):
    priority = 0.6
    changefreq = "weekly"

    def items(self):
        return [
            "ambadyestate_app:home",
            "ambadyestate_app:about_page",
            "ambadyestate_app:rooms_page",
            "ambadyestate_app:packages_page",
            "ambadyestate_app:activities_page",
            "ambadyestate_app:blog_page",
            "ambadyestate_app:contact_page",
            "ambadyestate_app:gallery",
            "ambadyestate_app:nearby_destinations_page",
        ]

    def location(self, item):
        return reverse(item)


# --------- Rooms ---------
class RoomSitemap(AmbadyEstateSitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Room.objects.filter(status="active")

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("ambadyestate_app:room_details", kwargs={"slug": obj.slug})


# --------- Activities ---------
class ActivitySitemap(AmbadyEstateSitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Activity.objects.filter(status="active")

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("ambadyestate_app:activity_details", kwargs={"slug": obj.slug})


# --------- Nearby Destinations ---------
class NearbyDestinationSitemap(AmbadyEstateSitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return NearbyDestination.objects.filter(status="active")

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse(
            "ambadyestate_app:nearby_destination_details", kwargs={"slug": obj.slug}
        )


# --------- Packages ---------
class PackageSitemap(AmbadyEstateSitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Package.objects.filter(status="active")

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("ambadyestate_app:package_details", kwargs={"slug": obj.slug})


# --------- Blog ---------
class BlogSitemap(AmbadyEstateSitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse("ambadyestate_app:blog_details", kwargs={"slug": obj.slug})