from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('fetch_drt_data',views.ViewDRTDataViewSet,basename='fetch_drt_data')

urlpatterns = [ 

] + router.urls
