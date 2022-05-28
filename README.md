# install requirements
```
pip install -r requirements.txt
```

# first edit/create config.ini (in main repository dir & info_site dir)
```
[GOOGLE]
client_secret_file = client_secret.json

gs_file = test_sheet

[SQL]
alchemy_engine = postgresql+psycopg2://admin:passwd@localhost/db_name

[OPTIONS]
timer = 5
```

to get client_secret file create google api token (read pygsheets docs)
more info: https://pygsheets.readthedocs.io/en/stable/authorization.html

in gs_file paste your sheet name from google drive/sheets
# sqlalchemy engine example:
```
alchemy_engine = postgresql+psycopg2://username:password@host/db_name
```

run
```
# parser
python sheet_parser.py
# site
python sheet_parser/manage.py runserver
```