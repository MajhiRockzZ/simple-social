# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)