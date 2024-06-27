from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('person.urls', namespace='person')),
    path('admin/', admin.site.urls),
]
