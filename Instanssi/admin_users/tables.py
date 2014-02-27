# -*- coding: utf-8 -*-

import django_tables2 as tables
from Instanssi.dblog.models import DBLogEntry

class LogTable(tables.Table):
    class Meta:
        model = DBLogEntry
        exclude = ('id',)