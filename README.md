This is my first backend web-project to learn and try django framework.
It's pretty simple and was made to practice core django concepts as work with templates, models, migrations, ORM, database etc.
Here you will find list of index page, goods list with pagination, cart, order page, profile and simple authorization, about page. Each page have navigation bar and mini cart icon that opens mini cart modal window.
Authorization is simple but I also implemented change profile info and profile password, forget password systems. To recover password you can request for email message with a recovery link in it.

I tried to deploy it with Render and tested myself.

You can find some more small features in this project if you try it yourself.

If deployed on render:

predeploy commands:
python manage.py migrate && python manage.py createsuperuser --noinput || true

deploy commands:
pip install -r requirements.txt

start command:
gunicorn Crispy.wsgi:application

Environment Variables:
ALLOWED_HOSTS=my-app.onrender.com
DATABASE_URL=<auto-filled if Postgres linked>
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=vladvelvvv@gmail.com
DJANGO_SUPERUSER_PASSWORD=adminpassword

fixture also must be loaded for the good list to work or you can add your own goods and categories.

Here are some images of deployed web-site:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e7f629d3-3e37-40f4-b0d1-3ae9a8529108" /> index page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a9229597-5fae-4da2-8bac-6ed39fd685ad" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c4de5a0d-c259-4ef9-99a9-17f3db12c88d" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5f207217-bfc0-4845-8c2d-23172c08c55d" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e557fadf-bb2b-4f85-957a-378e7a15175b" /> mini cart modal window
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9730c9a1-c9fc-42f2-870e-acfa52215350" /> cart
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5fa7c111-9044-4d0f-a2a5-707f18322f8f" /> login page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9dbe748f-bd4e-40b7-a21a-376ab8992e7a" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cc89d081-9147-4266-85f9-234c7b935a2e" /> registration page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a9028b68-49f6-4b91-b91f-050cbfc9b91e" /> find on map button
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0d5448af-6bcb-4806-bdb5-5cfdb5ae19d3" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/606a8ac2-f91c-4111-9edc-5938dff5afbb" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/49a0edc3-c35f-4aad-aabf-3e8b6506320e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/af3fdfac-a315-4f50-8635-9938e9a2615c" /> logged in message
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1d8ebbe4-b07b-4439-8336-0103166f0c75" /> profile page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7a7d011b-8a8d-4dca-84d6-5c95b2d11bfc" /> 
change profile info, change password and log out buttons with cart modal and orders window.


















