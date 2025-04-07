# Django Nuxt Starter

## 1. Production deployment
1. Create `.env` file at the root (from `.env.prod`):
   * `COMPOSE_PROJECT_NAME` - unique project name
   * `SQL_USER` - PostgreSQL database user
   * `WEB_PORT` - website port
2. Create secret files:
   * `secrets/key.txt` - Django [secret key](https://docs.djangoproject.com/en/5.2/ref/settings/#std-setting-SECRET_KEY)
   * `secrets/db.txt` - PostgreSQL database password
3. Edit some settings at backend/backend/settings.py:
   * `ALLOWED_HOSTS` - add or remove hosts at which the website is available
   * `SESSION_COOKIE_AGE` - authentication session lifetime (in seconds)
   * `PERIODIC_TASKS` - a list of periodic tasks
4. Build containers:
    ```shell
    $ ./bin/build.sh
    ```
   Containers will also be started after the command.

## 2. Development deployment
1. Create `.env` file at the root (from `.env.dev`).
   * `COMPOSE_PROJECT_NAME` - unique project name
   * `WEB_PORT` - website port
2. Start containers:
    ```shell
    $ ./bin/up.sh
    ```
3. Migrate database:
    ```shell
    $ ./bin/manage.sh migrate --noinput
    $ ./bin/manage.sh createcachetable
    ```
4. Enable periodic update (optional):
    ```shell
    $ ./bin/manage.sh enable-periodic
    ```

## 3. Stop containers
```shell
$ ./bin/down.sh
```

## 4 Remove DB volume (containers should be stopped)

Find PostgreSQL volume for the project (starts with $COMPOSE_PROJECT_NAME from .env)
"${COMPOSE_PROJECT_NAME}_pgdata_dev" for development mode or "${COMPOSE_PROJECT_NAME}_pgdata" for production:
```shell
$ docker volume ls
```
Then remove the volume
```shell
$ docker volume rm <volume_name>
```

### 5 Start containers if stopped
```shell
$ ./bin/up.sh
```

### 6 Rebuild running containers (for production mode only)
If DB migrations are possible then:
```shell
$ ./rebuild.sh
```
Otherwise, stop containers first, remove DB volume and build containers again:
```shell
$ ./build.sh
```