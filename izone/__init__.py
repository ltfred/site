from __future__ import absolute_import, unicode_literals

from pymysql import install_as_MySQLdb

install_as_MySQLdb()

from .celery import app as celery_app

__all__ = ("celery_app",)
