from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispositivoViewSet, LuogoViewSet, ManutenzioneViewSet, \
    SoftwareViewSet

# 1 Definiamo il router che raggruppa gli endpoint
router = DefaultRouter()

# 2 definiamo il gruppo di endpoint legati al "Dispositivo"
router.register(r'dispositivi', DispositivoViewSet, basename='dispositivo')
router.register(r'luoghi', LuogoViewSet)
router.register(r'manutenzioni', ManutenzioneViewSet)
router.register(r'software', SoftwareViewSet)
# la r davanti alla stringa dice a python di prendere quella stringa raw cioè
# senza sequenze di escape come ad esempio \n \s \t


# 3 definiamo urls
urlpatterns = [
    path('', include(router.urls)),
]

