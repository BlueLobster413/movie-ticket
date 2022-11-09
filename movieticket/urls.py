
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('system/', admin.site.urls),
    # path('admin/',include("admin.urls")),
    path('', include("booking.urls")),
    path('users/', include("accounts.urls")),
    path('admin/', include("webadmin.urls")),
]
