Django coffee-shop project
# Run locally  :rocket:

To start projetc locally:
```bash
python manage.py runserver
```
Link: 
http://127.0.0.1:8000
Admin:
http://127.0.0.1:8000/admin

# Run in Docker🐳
```bash
docker build -t coffee-shop .
docker run -p 8000:8000 coffee-shop
```
Link: 
http://localhost:8000
Admin:
http://localhost:8000/admin

Login: admin
Password: admin

