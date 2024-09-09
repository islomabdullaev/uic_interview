from django.urls import path
from petrol_spy.views import LeadDashboardAPIView

urlpatterns = [
    path('leaderboard/', LeadDashboardAPIView.as_view())
]