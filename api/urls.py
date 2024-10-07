from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllocationViewSet, PeriodViewSet, QRVerifyView, MealViewSet, LogoutView, IsAuthenticated, UserDetail, QRVerifyUpdateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Mess Website API",
      default_version='v1',
      description="API for the Mess Website",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ep230051013@iiti.ac.in"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'allocation', AllocationViewSet)
router.register(r'period', PeriodViewSet)
router.register(r'meal', MealViewSet)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('auth/user/', UserDetail.as_view(), name='user_detail'),
    path('auth/login/', obtain_auth_token, name='api_token_auth'),
    path('auth/logout/', LogoutView.as_view(), name='api_token_logout'),
    path('auth/is_authenticated/', IsAuthenticated.as_view(), name='is_authenticated'),
    path('qrverify/<int:id>/', QRVerifyView.as_view(), name='qrverify'),
    path('qrverify/scan/', QRVerifyUpdateView.as_view(), name='qrverify_update'),
]
