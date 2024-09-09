from rest_framework import serializers
from django.contrib.auth.models import User


class LeaderDashboardSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    reports_count = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ('id', 'display_name', 'reports_count')

    def get_display_name(self, obj):
        try:
            return obj.oneid_profile.full_name
        except Exception:
            return obj.username
    
    def get_reports_count(self, obj):
        return obj.reports.all().count()