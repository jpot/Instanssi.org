from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .admin.viewsets.events import AdminEventViewSet
from .admin.viewsets.kompomaatti import AdminCompoEntryViewSet, AdminCompoViewSet
from .ical.feed import EventFeed
from .viewsets.kompomaatti import (
    CompetitionParticipationViewSet,
    CompetitionViewSet,
    CompoEntryViewSet,
    CompoViewSet,
    EventViewSet,
    TicketVoteCodeViewSet,
    UserCompetitionParticipationViewSet,
    UserCompoEntryViewSet,
    VoteCodeRequestViewSet,
    VoteGroupViewSet,
)
from .viewsets.programme import ProgrammeEventViewSet
from .viewsets.store import StoreItemViewSet, StoreTransactionViewSet
from .viewsets.user import CurrentUserViewSet

app_name = "api"


class InstanssiAPIRoot(routers.APIRootView):
    """
    This is the v1 Instanssi API. Most things work only for logged in users.
    """

    pass


class CustomRouter(routers.DefaultRouter):
    APIRootView = InstanssiAPIRoot


router = CustomRouter()

# Public API
router.register(r"events", EventViewSet, basename="events")
router.register(r"competitions", CompetitionViewSet, basename="competitions")
router.register(
    r"competition_participations",
    CompetitionParticipationViewSet,
    basename="competition_participations",
)
router.register(r"user_participations", UserCompetitionParticipationViewSet, basename="user_participations")
router.register(r"compos", CompoViewSet, basename="compos")
router.register(r"compo_entries", CompoEntryViewSet, basename="compo_entries")
router.register(r"user_entries", UserCompoEntryViewSet, basename="user_entries")
router.register(r"programme_events", ProgrammeEventViewSet, basename="programme_events")
router.register(r"store_items", StoreItemViewSet, basename="store_items")
router.register(r"store_transaction", StoreTransactionViewSet, basename="store_transaction")
router.register(r"current_user", CurrentUserViewSet, basename="current_user")
router.register(r"user_vote_codes", TicketVoteCodeViewSet, basename="user_vote_codes")
router.register(r"user_vote_code_requests", VoteCodeRequestViewSet, basename="user_vote_code_requests")
router.register(r"user_votes", VoteGroupViewSet, basename="user_votes")

# Admin API (requires admin privileges)
router.register("admin/events", AdminEventViewSet, basename="admin_events")
router.register("admin/compos", AdminCompoViewSet, basename="admin_compos")
router.register("admin/compo_entries", AdminCompoEntryViewSet, basename="admin_compo_entries")

urlpatterns = [
    path("ics/instanssi.ics", EventFeed(), name="ics_feed"),
    path("", include(router.urls)),
]
