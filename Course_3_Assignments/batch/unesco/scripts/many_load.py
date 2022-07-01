import csv
from unicodedata import category  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Iso, Region,State, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()


    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])
        s, created = State.objects.get_or_create(name=row[8])
        #site, created = Site.objects.get_or_create(name=row[10])
        try :
            area =  int(row[6])
        except:
            area = None

        site = Site(name = row[0], year = row[3], latitude = row[5], longitude = row[4], description=row[1], justification=row[2], area_hectares=area, category =c, iso = i, region = r, state = s)
        site.save()
        

        