from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from django.conf import settings
from django.conf.urls.static import static
from restauth.api import auth_router
from restauth.authorization import AuthBearer
from MyStore.api import category__router, product_router,cart_router, wishlist_router, colorLogo__router

api = NinjaAPI(
    title='MyStore',
    version='0.1',
    csrf=False,
)

api.add_router('category/', category__router)
api.add_router('product/', product_router)
api.add_router('auth/', auth_router)
api.add_router('colorLogo/', colorLogo__router)
api.add_router('cart/', cart_router, auth=AuthBearer())
api.add_router('wishlist/', wishlist_router, auth=AuthBearer())


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
