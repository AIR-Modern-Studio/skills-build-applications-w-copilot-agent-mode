from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

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
    user_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    total_points = serializers.IntegerField(source='score', read_only=True)
    activity_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'user_name', 'team_name', 'score', 'total_points', 'rank', 'activity_count']
    
    def get_user_name(self, obj):
        return obj.user.name if obj.user else None
    
    def get_team_name(self, obj):
        return obj.user.team.name if obj.user and obj.user.team else None
    
    def get_activity_count(self, obj):
        return obj.user.activities.count() if obj.user else 0
