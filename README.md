## Supported tags and respective `Dockerfile` links

* [`python3.6` _(Dockerfile)_](https://github.com/berndverst/uwsgi-nginx-flask-falcon/blob/master/python3.6/Dockerfile)
* [`python3.6-index` _(Dockerfile)_](https://github.com/berndverst/uwsgi-nginx-flask-falcon/blob/master/python3.6-index/Dockerfile)

# uwsgi-nginx-falcon

**Docker** image with **uWSGI** and **Nginx** for **Falcon** web applications in **Python 3.6** running in a single container.

## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Falcon**](https://falconframework.org/) web applications in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

uWSGI with Nginx is one of the best ways to deploy a Python web application, so you you should have a [good performance (check the benchmarks)](http://nichol.as/benchmark-of-python-web-servers) with this image.

**GitHub repo**: <https://github.com/berndverst/uwsgi-nginx-falcon-docker>

**Docker Hub image**: <https://hub.docker.com/r/berndverst/uwsgi-nginx-falcon/>


For more information, including configuration options see https://github.com/tiangolo/uwsgi-nginx-docker and https://github.com/tiangolo/uwsgi-nginx-flask-docker on which this project is based.

## License

This project is licensed under the terms of the Apache license.
