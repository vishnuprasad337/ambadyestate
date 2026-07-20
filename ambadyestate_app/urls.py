from django.urls import path
from . import views

app_name = "ambadyestate_app"

urlpatterns = [
    path("login/", views.admin_login, name="admin_login"),
    path("dashboard/", views.admin_dashboard, name="dashboard"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),
    #Blogs
    path("blogs/", views.blog_list, name="blog_list"),
    path("blogs/create/", views.blog_create, name="blog_create"),
    path("blogs/<slug:slug>/update/", views.blog_update, name="blog_update"),
    path("blogs/<slug:slug>/delete/", views.blog_delete, name="blog_delete"),
    #Testimonials

     path("testimonials/", views.testimonial_list, name="testimonial_list"),
    path("add-review", views.testimonial_create, name="testimonial_create"),
    path(
        "testimonials/<int:pk>/edit/",
        views.testimonial_update,
        name="testimonial_update",
    ),
    path(
        "testimonials/<int:pk>/delete/",
        views.testimonial_delete,
        name="testimonial_delete",
    ),
    path("categories/", views.category_list, name="category_list"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/update/<int:pk>/", views.update_category, name="update_category"),
    path("categories/delete/<int:pk>/", views.delete_category, name="delete_category"),
    path("list-images/", views.gallery_images, name="list_image"),
path("add_image/", views.add_image, name="add_image"),
path("delete-image/<int:image_id>/", views.delete_image, name="delete_image"),

path("rooms/", views.room_list, name="room_list"),
    path("rooms/add/", views.room_add, name="room_add"),
    path("rooms/<slug:slug>/", views.room_detail, name="room_detail"),
    path("rooms/<slug:slug>/edit/", views.room_edit, name="room_edit"),
    path("rooms/<slug:slug>/delete/", views.room_delete, name="room_delete"),
    path("activities/", views.activity_list, name="activity_list"),
    path("activities/add/", views.activity_create, name="activity_create"),
    path("activities/<slug:slug>/", views.activity_detail, name="activity_detail"),
    path("activities/<slug:slug>/edit/", views.activity_update, name="activity_update"),
    path("activities/<slug:slug>/delete/", views.activity_delete, name="activity_delete"),

    path(
        "nearby-destinations/",
        views.nearby_destination_list,
        name="nearby_destination_list",
    ),
    path(
        "nearby-destinations/add/",
        views.nearby_destination_create,
        name="nearby_destination_create",
    ),
    path(
        "nearby-destinations/<slug:slug>/",
        views.nearby_destination_detail,
        name="nearby_destination_detail",
    ),
    path(
        "nearby-destinations/<slug:slug>/edit/",
        views.nearby_destination_update,
        name="nearby_destination_update",
    ),
    path(
        "nearby-destinations/<slug:slug>/delete/",
        views.nearby_destination_delete,
        name="nearby_destination_delete",
    ),

     path("packages/", views.package_list, name="package_list"),
    path("packages/add/", views.package_create, name="package_create"),
    path("packages/<slug:slug>/", views.package_detail, name="package_detail"),
    path("packages/<slug:slug>/edit/", views.package_update, name="package_update"),
    path("packages/<slug:slug>/delete/", views.package_delete, name="package_delete"),
    path("reservations/book/", views.reservation_create, name="reservation_create"),

    
    path("reservations/", views.reservation_list, name="reservation_list"),
    path("reservations/<int:pk>/delete/", views.reservation_delete, name="reservation_delete"),
        path("contact/", views.contact_view, name="contact"),
 
    # Staff — list page; reply/edit/delete are modals on this same page
    path("enquiries/", views.enquiry_list, name="enquiry_list"),
    path("enquiries/<int:pk>/reply/", views.enquiry_reply, name="enquiry_reply"),
    path("enquiries/<int:pk>/edit/", views.enquiry_update, name="enquiry_update"),
    path("enquiries/<int:pk>/delete/", views.enquiry_delete, name="enquiry_delete"),
    path("enquiries/add/", views.contact_view, name="enquiry_add"),
    path('booking/', views.booking_page, name='booking_page'),


#FRONTEND#


     path('', views.home, name='home'), 
     path('about-us/', views.about_page, name='about_page'),
     path('stays/', views.rooms_page, name='rooms_page'),
path('stays/<slug:slug>/', views.room_details, name='room_details'),
path('package/', views.packages_page, name='packages_page'),
path('package/<slug:slug>/', views.package_details, name='package_details'),
path("activity/", views.activities_page, name="activities_page"),
    path("activity/<slug:slug>/", views.activity_details, name="activity_details"),
path('blog/', views.blog_page, name='blog_page'),
path('blog/<slug:slug>/', views.blog_details, name='blog_details'),
path('contacts/', views.contact_page, name='contact_page'),
path(
    "nearby-destination/<slug:slug>/",
    views.nearby_destination_details,
    name="nearby_destination_details",

),
path("gallery/", views.gallery, name="gallery"),

]

handler404 = "ambadyestate_app.views.page_404"