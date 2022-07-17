To run project:

NOTE: 
- I deployed this project on Heroku
  ( http://arabic-writers.herokuapp.com/ )

1 - Clone project from GitHub 
    
    git clone https://github.com/Mahmoud59/arabic-writers.git

2 - In project directory beside requirements' directory, 
    create a virtual environment by 

    virtualenv venv
    source venv/bin/activate

3 - Install packages in virtual environment by 

    pip install -r src/requirements.txt

    pip install -r requirements/test-requirements.txt 

4 - For list xlsx file data (127.0.0.1:8000/api/v1/arabic-writers/) GET
    Or with Heroku ( http://arabic-writers.herokuapp.com/api/v1/arabic-writers/ )

5 - For add new row to xlsx file (127.0.0.1:8000/api/v1/arabic-writers/) POST
    Or with Heroku ( http://arabic-writers.herokuapp.com/api/v1/arabic-writers/ )

6 - For retrieve xlsx file data (127.0.0.1:8000/api/v1/arabic-writers/'arabic-writers-id'/) GET
    Or with Heroku ( http://arabic-writers.herokuapp.com/api/v1/arabic-writers/'arabic-writers-id'/ )

7 - For modify xlsx file data (127.0.0.1:8000/api/v1/arabic-writers/'arabic-writers-id'/) PATCH
    Or with Heroku ( http://arabic-writers.herokuapp.com/api/v1/arabic-writers/'arabic-writers-id'/ )

8 - For delete xlsx file row (127.0.0.1:8000/api/v1/arabic-writers/'arabic-writers-id'/) DELETE
    Or with Heroku ( http://arabic-writers.herokuapp.com/api/v1/arabic-writers/'arabic-writers-id'/ )

7 - For run unit test, run `pytest` in apps src directory.

8 - You can run `flake8 --statistics` for characters limited in one line.

9 - You can run `isort .` for sort importing packages, function, and classes.