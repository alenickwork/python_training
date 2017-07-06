# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #4: refactor for fixture usage
"""
import os

from model.contact import Contact

def test_add_contact(app):

    app.session.login(username = "admin",
              password = "secret")
    app.contact.create(Contact(firstname = "test_fn",
                                    middlename = "test_mn",
                                    lastname = "test_ln",
                                    nickname = "test_nn",
                                    photo_link = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                              "data",
                                                              "Cute-White-Pigeon-Display-Picture.jpg"),
                                    title = "test_title",
                                    company = "test_c",
                                    address = "test_addr",
                                    home_phone = "test_hph",
                                    mobile_phone = "test_mph",
                                    work_phone = "test_wph",
                                    fax = "test_fx",
                                    email_prior = "test_em1",
                                    email_2 = "test_e2",
                                    email_3 = "test_e3",
                                    homepage = "test_hp",
                                    birthday_day = "15",
                                    birthday_month="March",
                                    birthday_year="1982",
                                    anniversary_day = "30",
                                    anniversary_month="April",
                                    anniversary_year="2011",
                                    address_secondary = "test_addr2",
                                    phone_secondary = "test_ph2",
                                    notes = "12121221")
                            )
    app.session.logout()