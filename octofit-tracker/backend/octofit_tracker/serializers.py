from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class TeamSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    total_points = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'member_count', 'total_points']
    
    def get_member_count(self, obj):
        """Return the count of users in this team"""
        return obj.members.count()
    
    def get_total_points(self, obj):
        """Calculate total points from all team members' activities"""
        from django.db.models import Sum
        # Sum calories burned from all activities of team members
        result = Activity.objects.filter(user__team=obj).aggregate(
            total=Sum('calories_burned')
        )
        return result['total'] or 0

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_superhero', 'team', 'team_id']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    workout = WorkoutSerializer(read_only=True)
    workout_id = serializers.PrimaryKeyRelatedField(queryset=Workout.objects.all(), source='workout', write_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'workout', 'workout_id', 'date', 'duration_minutes', 'calories_burned']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score', 'rank']
