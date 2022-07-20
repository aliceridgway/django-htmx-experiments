# exec(open("scripts/create_fake_data.py").read())
import random

from faker import Faker
from core.models import ToDo

fake: Faker = Faker()

for i in range(100):
    todo = ToDo.objects.create(
        name=fake.paragraph(nb_sentences=1),
        status=random.choice(ToDo.StatusChoice.choices)[0],
    )
    print(f"Created todo. Name: {todo.name}  Status: {todo.status}")

todo_count = ToDo.objects.count()

print(f"There are {todo_count} todos in the database")
