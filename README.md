# Jobsz

The following instructions will guide you to clone and run the project..

### Prerequisites

- Python 3+
- Virtualenv

### Installing


#### Install dependencies
```
pip install -r requirements.txt
```

#### Run fixtures and Create database
```
bash run_fixtures.sh
```
```
python manage.py migrate
```
### Run fixtures2
if for some reason the command: bash run_fixtures.sh not work.
Run:
```
python manage.py loaddata salary_range.yaml and python manage.py loaddata required_degree.yaml
```

#### Run application
```
python manage.py runserver
```
