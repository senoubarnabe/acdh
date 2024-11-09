from django.urls import path
from .views import index , postuler_views, temo_views, propos_views, confirmation_views

urlpatterns = [
    path("", index , name="index"),
    path("postuler/",postuler_views, name="postuler"),
    path("témoignages/",temo_views , name="temo"),
    path("propos/", propos_views, name="propos"),
    path("confirmation/", confirmation_views, name="confirmation"),
]