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
