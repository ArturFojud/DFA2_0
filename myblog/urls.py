#from django.contrib import admin
#from django.urls import path, include
#from . import old_views
#from django.urls import path, include

#urlpatterns = [
#    path('onas/', old_views.onas),
#    path('', old_views.blog),
#    path('', include('app_blog2.urls')),
#    path('admin/', admin.site.urls),
#]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_blog2.urls')),
]
