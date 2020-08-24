pip3 install virtualenv
virtualenv --version
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate

pip3 install -r requirements.txt
python3 ./manage.py runserver

http://localhost:8000/twitter/
    
