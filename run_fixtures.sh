for file in */fixtures/*.yaml; do python manage.py loaddata "$file"; done
