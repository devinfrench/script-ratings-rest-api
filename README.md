# Script Ratings REST API

## Pipenv Setup

```bash
$ pipenv shell
$ pipenv install
$ python
>> from app import db
>> db.create_all()
>> exit()

$ python app.py
```

## Endpoints

-   GET /ratings
-   GET /ratings/:script
-   POST /rating
-   PUT /rating
-   DELETE /rating
