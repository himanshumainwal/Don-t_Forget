from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("", views.user_logIn, name='logIn'),
    path("register/", views.register, name='register'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("details/", views.add_details, name='add_details'),
    path("view_details/", views.view_details, name='view_details'),
    path("delete_info/<id>/", views.delete_info, name='delete_info'),
    path("edit_info/<id>/", views.edit_info, name='edit_info'),
    path('logout/', views.user_logout, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()