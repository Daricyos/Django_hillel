from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('students.urls')),
    path('', include('teacher.urls')),
    path('', include('group.urls')),
    path('', include('sending_email.urls')),
    path('', include('currency.urls')),
]
