# Django Ninja + PostgreSQL + MongoDB + Redis + Celery

## RESTful APIS ###
Developed RESTful APIs using Django Ninja.

## PostgreSQL

Database name is <b>"ms_cinema"</b>

### Environment Variables
<code>
<pre>
POSTGRES_NAME="ms_cinema"       // Database name
POSTGRES_USER="postgres"        // Username
POSTGRES_PASSWORD="password"    // Password
POSTGRES_HOST="127.0.0.1"       // Host
POSTGRES_PORT="5432"            // Port
</pre>
</code>
## MongoDB

Collection name is <b>"ms_cinema"</b>
### Environment Variables
<code>
<pre>
MONGO_NAME="ms_cinema"          // Database name
MONGO_USER=""                   // Username
MONGO_PASSWORD=""               // Password
MONGO_HOST="127.0.0.1"          // Host
MONGO_PORT="27017"              // Port
</pre>
</code>

## Running Server
<code>
<pre>
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py migrate --database sync_mongo
$ python manage.py runserver
</pre>
</code>

## Celer & Redis

- Broker: Redis
- Producer: Redis
### Worker
<code>
<pre>
$ celery -A ms_cinema worker -l info
</pre>
</code>

### Beat
<code>
<pre>
$ celery -A ms_cinema beat -l info
</pre>
</code>

## PyTest
Unit testing about models and views.
<code>
<pre>
$ pytest
</pre>
</code>
