from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard
from .serializers import UserSerializer, TeamSerializer, WorkoutSerializer, ActivitySerializer, LeaderboardSerializer
import json

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy', points_per_minute=8, category='Strength')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Pushups')
        self.assertEqual(self.workout.points_per_minute, 8)
        self.assertEqual(self.workout.category, 'Strength')

class ActivityModelTest(TestCase):
    def setUp(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Batman', email='batman@dc.com', team=team, is_superhero=True)
        workout = Workout.objects.create(name='Situps', description='Core', difficulty='Medium', points_per_minute=10, category='Core')
        self.activity = Activity.objects.create(user=user, workout=workout, duration_minutes=30, calories_burned=200)

    def test_activity_creation(self):
        self.assertEqual(self.activity.duration_minutes, 30)

class LeaderboardModelTest(TestCase):
    def setUp(self):
        team = Team.objects.create(name='Avengers', description='Avengers Team')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team, is_superhero=True)
        self.leaderboard = Leaderboard.objects.create(user=user, score=1000, rank=1)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.rank, 1)

class SerializerObjectIdTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='X-Men', description='X-Men Team')
        self.user = User.objects.create(name='Wolverine', email='wolverine@xmen.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration_minutes=45, calories_burned=300)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=500, rank=2)

    def test_team_serializer_id_is_string(self):
        serializer = TeamSerializer(self.team)
        data = serializer.data
        # Verify id field exists and is a string
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)
        # Verify JSON serialization works
        json_str = json.dumps(data)
        self.assertIsInstance(json_str, str)

    def test_user_serializer_id_is_string(self):
        serializer = UserSerializer(self.user)
        data = serializer.data
        # Verify id field exists and is a string
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)
        # Verify nested team id is also a string
        self.assertIn('team', data)
        self.assertIn('id', data['team'])
        self.assertIsInstance(data['team']['id'], str)
        # Verify JSON serialization works
        json_str = json.dumps(data)
        self.assertIsInstance(json_str, str)

    def test_workout_serializer_id_is_string(self):
        serializer = WorkoutSerializer(self.workout)
        data = serializer.data
        # Verify id field exists and is a string
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)
        # Verify JSON serialization works
        json_str = json.dumps(data)
        self.assertIsInstance(json_str, str)

    def test_activity_serializer_id_is_string(self):
        serializer = ActivitySerializer(self.activity)
        data = serializer.data
        # Verify id field exists and is a string
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)
        # Verify nested user and workout ids are strings
        self.assertIn('user', data)
        self.assertIn('id', data['user'])
        self.assertIsInstance(data['user']['id'], str)
        self.assertIn('workout', data)
        self.assertIn('id', data['workout'])
        self.assertIsInstance(data['workout']['id'], str)
        # Verify JSON serialization works
        json_str = json.dumps(data)
        self.assertIsInstance(json_str, str)

    def test_leaderboard_serializer_id_is_string(self):
        serializer = LeaderboardSerializer(self.leaderboard)
        data = serializer.data
        # Verify id field exists and is a string
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], str)
        # Verify nested user id is a string
        self.assertIn('user', data)
        self.assertIn('id', data['user'])
        self.assertIsInstance(data['user']['id'], str)
        # Verify JSON serialization works
        json_str = json.dumps(data)
        self.assertIsInstance(json_str, str)
