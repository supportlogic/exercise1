PYTHON = ./xfind/manage.py
VENV_PYTHON = ./venv/bin/python
USER = naomi

createuser:
	$(VENV_PYTHON) $(PYTHON) shell -c "from django.contrib.auth.models import User; User.objects.create_user('$(USER)', password='$(USER)') if not User.objects.filter(username='$(USER)').exists() else None"
	$(VENV_PYTHON) $(PYTHON) shell -c "from mlapp.models import Customer; Customer.objects.create(name='$(USER)') if not Customer.objects.filter(name='$(USER)').exists() else None"
