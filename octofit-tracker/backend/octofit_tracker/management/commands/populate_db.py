from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Limpando dados antigos...')
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.user.delete_many({})
        db.team.delete_many({})
        db.workout.delete_many({})
        client.close()

        self.stdout.write('Criando times...')
        marvel = Team.objects.create(name='Marvel', description='Time Marvel')
        dc = Team.objects.create(name='DC', description='Time DC')

        self.stdout.write('Criando usuários...')
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True)

        self.stdout.write('Criando treinos...')
        pushups = Workout.objects.create(name='Pushups', description='Flexões', difficulty='Fácil', points_per_minute=8, category='Strength')
        situps = Workout.objects.create(name='Situps', description='Abdominais', difficulty='Médio', points_per_minute=10, category='Core')
        running = Workout.objects.create(name='Running', description='Corrida', difficulty='Difícil', points_per_minute=12, category='Cardio')

        self.stdout.write('Criando atividades...')
        Activity.objects.create(user=spiderman, workout=pushups, duration_minutes=30, calories_burned=200)
        Activity.objects.create(user=ironman, workout=situps, duration_minutes=25, calories_burned=180)
        Activity.objects.create(user=batman, workout=running, duration_minutes=40, calories_burned=350)
        Activity.objects.create(user=wonderwoman, workout=pushups, duration_minutes=35, calories_burned=220)

        self.stdout.write('Criando leaderboard...')
        Leaderboard.objects.create(user=spiderman, score=1200, rank=1)
        Leaderboard.objects.create(user=ironman, score=1100, rank=2)
        Leaderboard.objects.create(user=batman, score=1050, rank=3)
        Leaderboard.objects.create(user=wonderwoman, score=1000, rank=4)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))

        # Criar índice único em email usando pymongo
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.user.create_index([('email', 1)], unique=True)
        client.close()
        self.stdout.write(self.style.SUCCESS('Índice único em email criado na coleção user!'))
