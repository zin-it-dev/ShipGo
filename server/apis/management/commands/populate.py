import random

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from apis.factories import CategoryFactory, CourseFactory, LessonFactory

class Command(BaseCommand):
    help = "Generate fake data and seed the models with them."

    def add_arguments(self, parser):
        parser.add_argument('--amount', help="The amount of fake data you want", type=int)

    def handle(self, *args, **options):
        amount = options.get('amount', 10)
        
        categories = CategoryFactory.create_batch(amount)

        for _ in range(amount):
            try:
                course = CourseFactory(category=random.choice(categories))
                LessonFactory.create_batch(random.randint(2, 5), course=course)
            except ObjectDoesNotExist:
                raise CommandError('Models does not exist')

        self.stdout.write(self.style.SUCCESS("Generated models successfully!"))