# Stamp

: Pinterest MVP 2 hour project

* [demo and all endpoints](https://www.cecinestpasun.site)

## Description

```
$ MYSQL_USER=stamp_dev MYSQL_PWD=stamp_dev_pwd \
MYSQL_HOST=localhost MYSQL_DB=stamp_dev_db \
python3 -m main_app.app
```

## Environment

* __OS:__ Linux Ubuntu 14.04 LTS
* __languages:__ Python 3.4.3, Javascript, HTML, CSS
* __web server:__ nginx/1.4.6
* __application server:__ Flask==0.12.2, Jinja2==2.9.6
* __web server gateway:__ gunicorn (version 19.7.1)
* __database:__ mysql Ver 14.14 Distrib 5.7.18
* __JSON Web Token:__ PyJWT==1.4.2
* __documentation:__ Swagger (flasgger==0.6.6)
* __style:__
  * __python:__ PEP 8 (v. 1.7.0)
  * __web static:__ [W3C Validator](https://validator.w3.org/)
  * __bash:__ ShellCheck 0.3.3
  * __JavaScript:__ semistandard 11.0.0

## Configuration Files

The `/config/` directory contains configuration files for `nginx` and the
Upstart scripts.  The nginx configuration file is for the configuration file in
the path: `/etc/nginx/sites-available/default`.  The enabled site is a sym link
to that configuration file.  The upstart script should be saved in the path:
`/etc/init/[FILE_NAME.conf]`.  To begin this service, execute:

```
$ sudo start airbnb.conf
```
This script's main task is to execute the following `gunicorn` command:

```
$ gunicorn --bind 127.0.0.1:8001 wsgi.wsgi_airbnb:app.app
```

The `gunicorn` command starts an instance of a Flask Application.

---

### Web Server Gateway Interface (WSGI)

All integration with gunicorn occurs with `Upstart` `.conf` files.  The python
code for the WSGI is listed in the `/wsgi/` directory.  These python files run
the designated Flask Application.

## Setup

This project comes with various setup scripts to support automation, especially
during maintanence or to scale the entire project.  The following files are the
setupfiles along with a brief explanation:

* **`dev/setup.sql`:** Drops test and dev databases, and then reinitializes
the database.

  * Usage: `$ cat dev/bd/drop_recreate_dev_test_db.sql | mysql -uroot -p`

* **`3-deploy_web_static.py`:** uses 2 functions from (1-pack_web_static.py &
  2-do_deploy_web_static.py) that use the fabric3 python integration, to create
  a `.tgz` file on local host of all the local web static fils, and then calls
  the other function to deploy the compressed web static files.  Command must
  be executed from the `AirBnB_clone` root directory.

  * Usage: `$ fab -f 3-deploy_web_static.py deploy -i ~/.ssh/holberton -u ubuntu`

## Authors

* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/) | [@djohncoleman](https://twitter.com/djohncoleman)

## License

MIT License
