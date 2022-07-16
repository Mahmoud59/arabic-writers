To run project:

1 - Clone project from GitHub 
    
    git clone https://github.com/Mahmoud59/arabic-writers.git

2 - In project directory beside requirements' directory, 
    create a virtual environment by 

    virtualenv venv
    source venv/bin/activate

3 - Install packages in virtual environment by 

    pip install -r requirements/requirements.txt

    pip install -r requirements/test-requirements.txt 

4 - For list csv file data (127.0.0.1:8000/api/v1/arabic-writers/) GET

5 - For add new row to csv file (127.0.0.1:8000/api/v1/arabic-writers/) POST

6 - For retrieve csv file data (127.0.0.1:8000/api/v1/arabic-writers/'arabic-writers-id'/) GET

7 - For modify csv file data (127.0.0.1:8000/api/v1/arabic-writers/'arabic-writers-id'/) PATCH

8 - For delete csv file row (127.0.0.1:8000/api/v1/arabic-writers/'arabic-writers-id'/) DELETE

7 - For run unit test, run `pytest` in apps src directory.

8 - You can run `flake8 --statistics` for characters limited in one line.

9 - You can run `isort .` for sort importing packages, function, and classes.