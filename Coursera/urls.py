
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler403, handler500

handler404 = 'courses.views.view_404'
handler500 = 'courses.views.view_500'
handler403 = 'courses.views.view_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls',namespace='courses')),
    path('', include('blog.urls',namespace='blogs')),
    path('', include('users.urls',namespace='users')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
