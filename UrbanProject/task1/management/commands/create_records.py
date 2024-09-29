from django.core.management.base import BaseCommand
from task1.models import Buyer, Game


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Создаем 3 записи Buyer
        buyer1 = Buyer.objects.create(name="JohnDoe", balance=100.00, age=25)
        buyer2 = Buyer.objects.create(name="JaneSmith", balance=150.50, age=17)  # Младше 18 лет
        buyer3 = Buyer.objects.create(name="SamGreen", balance=200.00, age=30)

        # Создаем 3 записи Game
        game1 = Game.objects.create(title="AdventureQuest", cost=49.99, size=15.5, description="A thrilling adventure.", age_limited=False)  # Без ограничения возраста
        game2 = Game.objects.create(title="HorrorStory", cost=59.99, size=20.2, description="A terrifying horror game.", age_limited=True)
        game3 = Game.objects.create(title="SpaceOdyssey", cost=39.99, size=10.0, description="Explore the universe.", age_limited=True)

        # Buyer1 покупает все игры
        game1.buyers.set([buyer1])
        game2.buyers.set([buyer1])
        game3.buyers.set([buyer1])

        # Buyer2 (младше 18) получает только игру без ограничения возраста
        game1.buyers.add(buyer2)

        # Buyer3 покупает все игры
        game1.buyers.add(buyer3)
        game2.buyers.add(buyer3)
        game3.buyers.add(buyer3)

        self.stdout.write(self.style.SUCCESS("Records created successfully"))
