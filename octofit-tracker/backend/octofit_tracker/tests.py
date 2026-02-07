from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Pushups')

class ActivityModelTest(TestCase):
    def setUp(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Batman', email='batman@dc.com', team=team, is_superhero=True)
        workout = Workout.objects.create(name='Situps', description='Core', difficulty='Medium')
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
