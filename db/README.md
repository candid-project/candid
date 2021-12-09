Setup local postgres instructions (Ubuntu):

Install postgres:
```sh
sudo apt-get install postgresql postgresql-contrib
```

You might need to run a `pg_ctl init` somewhere... I did but then it got very confusing and pg_ctl wouldn't let me start a service so I'm not sure if install postgresql did it immediately or if it was the pg_ctl init that did it.


Postgresql starts off with just a default superuser and you'll want to add yourself as a user to make things easier.  First become a superuser:
```sh
sudo su - postgres
```

Create the db:
```sh
createdb candid_postgres_local
```

Connect to the database server:
```sh
psql template1
```

Create the user and give yourself privileges:
```sh
template1=# CREATE USER {your user} WITH PASSWORD '{your password}';
template1=# GRANT ALL PRIVILEGES ON DATABASE candid_postgres_local to {your user};
template1=# \q
```

Then add your local database info to candid/env_template.sh, including including the environment variable `CLOUD_SQL_CONNECTION_NAME`.


You should now be able to connect to the db from your user account.  First log out of superuser with `exit`.  Then try connecting to the db with:
```sh
psql -d candid_postgres_local -U {your user}
```


Helpful resources:
https://www.cyberciti.biz/faq/howto-add-postgresql-user-account/
https://www.postgresql.org/docs/9.1/tutorial-createdb.html
