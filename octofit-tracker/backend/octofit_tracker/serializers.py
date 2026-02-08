from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.CharField(write_only=True, required=False, allow_null=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_superhero', 'team', 'team_id']
    
    def create(self, validated_data):
        team_id = validated_data.pop('team_id', None)
        if team_id:
            validated_data['team_id'] = team_id
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        team_id = validated_data.pop('team_id', None)
        if team_id:
            validated_data['team_id'] = team_id
        return super().update(instance, validated_data)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Workout
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)
    workout = WorkoutSerializer(read_only=True)
    workout_id = serializers.CharField(write_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'workout', 'workout_id', 'date', 'duration_minutes', 'calories_burned']
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        workout_id = validated_data.pop('workout_id')
        validated_data['user_id'] = user_id
        validated_data['workout_id'] = workout_id
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        workout_id = validated_data.pop('workout_id', None)
        if user_id:
            validated_data['user_id'] = user_id
        if workout_id:
            validated_data['workout_id'] = workout_id
        return super().update(instance, validated_data)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score', 'rank']
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        validated_data['user_id'] = user_id
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            validated_data['user_id'] = user_id
        return super().update(instance, validated_data)
