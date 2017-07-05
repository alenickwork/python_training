# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #6: delete group
"""

def test_delete_group(app):
    app.session.login(username = "admin",
              password = "secret")
    app.group.delete_first_group()
    app.session.logout()
