from django.contrib import admin
from django.urls import path, include   # ← añade include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),      # ← monta aquí las URLs de tu app
]
