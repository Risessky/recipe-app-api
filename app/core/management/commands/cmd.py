from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        testdict = {'name': 'ashar', "tags":
                    [{"name": "Thai"}, {"name": "Dinner"}]}
        res = testdict.pop('tags')
        # print(testdict)
        print(res)
