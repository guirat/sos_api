from django.urls import path, include
from rest_framework import routers

from event.api.views import EventViewSet, ParticipantViewSet, TicketViewSet

router = routers.DefaultRouter()

router.register(r'event', EventViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'Tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),

]