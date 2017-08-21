from django.core.management.base import BaseCommand, CommandError
from heros.models import Hero, HeroRole
from django.contrib.staticfiles import finders


class Command(BaseCommand):
    help = 'Update the Hero app models from pre-formatted data files'

    def remove_hero_models_data(self):
        HeroRole.objects.all().delete()
        Hero.objects.all().delete()

    def get_hero_icon_file_path(self, hero_name):
        return '/hero-icons/' + hero_name.lower().replace(' ', '_').replace("'", '') + '_vert.jpg'

    def update_hero_models(self, data_file):
        with open(data_file, 'r') as heros_data:
            for hero_data_line in heros_data:
                # Example hero data line : 'Anti Mage-Agility-Melee-Carry-Escape-Nuker/n'
                unpacked_hero_data = hero_data_line.strip().split('-')
                Hero.objects.create(
                    name=unpacked_hero_data[0],
                    category=unpacked_hero_data[1].lower(),
                    attack_type=unpacked_hero_data[2].lower(),
                    photo=self.get_hero_icon_file_path(unpacked_hero_data[0])
                )

    def update_hero_role_models(self, data_file):
        with open(data_file, 'r') as heros_data:
            for hero_data_line in heros_data:
                unpacked_hero_data = hero_data_line.strip().split('-')
                hero = Hero.objects.get(name=unpacked_hero_data[0])
                for role in unpacked_hero_data[3:]:
                    HeroRole.objects.create(hero=hero, role=role.lower())

    def handle(self, *args, **options):

        self.stdout.write('Starting to Update Hero and Hero Role Models.')
        self.stdout.write('Finding pre-formatted Hero data files...')
        data_file = finders.find('data/hero_data.txt')
        if not data_file:
            raise CommandError('Unable to file pre-formatted Hero data file "hero_data.txt".')

        self.stdout.write('Removing previous Model Data.')
        self.remove_hero_models_data()

        self.stdout.write('Starting to update Hero Model.')
        self.update_hero_models(data_file)
        self.stdout.write("Hero Model has been updated.")

        self.stdout.write("Starting to update HeroRole Model.")
        self.update_hero_role_models(data_file)
        self.stdout.write("HeroRole Model has been updated.")

        self.stdout.write('Command completed successfully.')
