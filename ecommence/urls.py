from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView, SpectacularRedocView
urlpatterns = [
    path('', include('ShopMit.urls')),
    path('users/', include("users.urls")),
    path('products/', include("products.urls")),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
