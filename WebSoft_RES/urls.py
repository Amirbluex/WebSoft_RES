from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from WebSoft_RES import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('', include('account.urls')),
    path('blog/', include('blog.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


