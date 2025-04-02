FROM python:3.11.2-alpine3.17

WORKDIR /migration

ADD migrations/ /migration/migrations
ADD alembic.ini /migration/

RUN pip install alembic==1.11.2 psycopg2-binary==2.9.6

ENTRYPOINT ["alembic", "upgrade", "5f7db58effe4"]