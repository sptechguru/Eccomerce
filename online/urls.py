

from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

admin.site.site_header ='$ SUPER SPTECH SHOP ??? '
admin.site.site_title = 'PAL SAHAB '
admin.site.index_title = '??? ... SUPER ONLINESHOP FOR SPTECH PAL .... ???'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('', include('shop.urls')),

    # fron page show in butoon click on blog and shop
    # path('', views.index)
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
