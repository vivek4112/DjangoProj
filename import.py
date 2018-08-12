import csv
import os,sys

project_dir = "c:/weread/weread"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'weread.settings'

import django
django.setup()

from readbooks.models import books

data = open("books.csv")
reader = csv.reader(data)

for row in reader:
	books.isbn = row[0]
	books.title = row[1]
	books.author = row[2]
	books.year = row[3]
	books.save()







