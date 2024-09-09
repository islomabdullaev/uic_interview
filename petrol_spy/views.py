from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from petrol_spy.serializers import LeaderDashboardSerializer
from django.db.models import Count, Q



class LeadDashboardAPIView(APIView):
    thirty_days_ago = timezone.now() - timedelta(days=30)
    def get(self, request):
        users = User.objects.annotate(
            reports_total_count=Count(
                "reports", filter=Q(reports__created_at__gte=self.thirty_days_ago)
                )).order_by("-reports_total_count", "id")[:100]
        serializer = LeaderDashboardSerializer(users, many=True)
        return Response(serializer.data)