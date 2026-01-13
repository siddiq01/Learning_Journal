import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_journal.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'Siddiq'
email = 'badlanis56@gmail.com'
password = 'Badlani@123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created successfully!")
else:
    print(f"Superuser {username} already exists.")