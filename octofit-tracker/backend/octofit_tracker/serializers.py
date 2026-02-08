from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from bson.errors import InvalidId


def validate_object_id(value):
    """Validate that a string is a valid ObjectId format."""
    if value is None:
        return value
    try:
        ObjectId(value)
        return value
    except (InvalidId, TypeError):
        raise serializers.ValidationError(f"'{value}' is not a valid ObjectId.")


class ObjectIdField(serializers.CharField):
    """Custom field that handles ObjectId serialization and validation."""
    
    def __init__(self, **kwargs):
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(validate_object_id)
        super().__init__(**kwargs)


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
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
    id = serializers.CharField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = ObjectIdField(write_only=True, required=False, allow_null=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_superhero', 'team', 'team_id']

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Workout
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = ObjectIdField(write_only=True)
    workout = WorkoutSerializer(read_only=True)
    workout_id = ObjectIdField(write_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'workout', 'workout_id', 'date', 'duration_minutes', 'calories_burned']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = ObjectIdField(write_only=True)
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
