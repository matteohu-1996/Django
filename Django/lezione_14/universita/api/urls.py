from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessoreViewSet, StudenteViewSet, CorsoViewSet

router = DefaultRouter()
router.register(r"professori", ProfessoreViewSet)
router.register(r"studenti", StudenteViewSet)
router.register(r"corsi", CorsoViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
