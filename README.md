# Test

### Install python3

	sudo apt install python3

### Install virtual environment

	sudo apt-get install python3-venv

### Create virtual environment

	python3 -m venv myvenv

### Activate virtual environment

	source myvenv/bin/activate

### Install Requirements

	python -m pip install --upgrade pip
	pip install -r requirements.txt

### Migrate

	python manage.py migrate

### Runserver

	python manage.py runserver

### Run in localhost

	Open localhost:8000 in your browser
	Add id_list and passenger_list as query parameters
	both id_list and passenger_list must contain a list of numbers
	Example: localhost:8000?id_list=[1,2]&passenger_list=[3,4]

### Run in postman
	Open Postman
	Use GET method
	Add localhost:8000 in request URL
	Add id_list and passenger_list in Params
	id_list and passenger_list must have a value of list of numbers
	Click Send

### Unit Test
	python manage.py test myapi

### Coverage
	coverage run myapi/functions.py
	cover report -m

### Explanation
	id_list and passenger_list values are partnered with respect to their index position
	For example:
	id_list = [1, 2]
	passenger_list = [3, 4]
	Index 0 of id_list is partnered to the Index 0 of passenger_list and
	Index 1 of id_list is partnered to the Index 1 of passenger_list
	Therefore, Airplane id number 1 have 3 passengers and Airplane id number 2 have 4 passengers

	In the scenario where their list sizes are not equal, the excess values will be ignored.