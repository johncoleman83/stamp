# Stamp

: Pinterest MVP 2 hour project

## Usage

* run server

```
$ MYSQL_USER=stamp_dev MYSQL_PWD=stamp_dev_pwd MYSQL_HOST=localhost \
MYSQL_DB=stamp_dev_db python3 -m main_app.app
```

* run api

```
MYSQL_USER=stamp_dev MYSQL_PWD=stamp_dev_pwd MYSQL_HOST=localhost \
MYSQL_DB=stamp_dev_db API_HOST=0.0.0.0 API_PORT=5001 python3 -m api.v1.app
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

## Author

* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/) | [@djohncoleman](https://twitter.com/djohncoleman)

## License

MIT License
