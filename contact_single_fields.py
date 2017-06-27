__author__ = "Elena Dimchenko"

import datetime

class Contact:
    def __init__(self, firstname,
                 middlename,
                 lastname,
                 nickname,
                 photo_link,
                 title,
                 company,
                 address,
                 home_phone,
                 mobile_phone,
                 work_phone,
                 fax,
                 email_prior,
                 email_2,
                 email_3,
                 homepage,
                 birthday_day,
                 birthday_month,
                 birthday_year,
                 anniversary_day,
                 anniversary_month,
                 anniversary_year,
                 address_secondary,
                 phone_secondary,
                 notes
                 ):
        """
        Contact record structure
        :param firstname:
        :param middlename:
        :param lastname:
        :param nickname:
        :param photo_link: TBD
        :param title:
        :param company:
        :param address:
        :param home_phone:
        :param mobile_phone:
        :param fax:
        :param email_prior:
        :param email_2:
        :param email_3:
        :param homepage:
        :param birthday_date:  must be like dd-mm-yyyy
        :param anniversary_date:
        :param address_secondary:
        :param phone_secondary:
        :param notes:
        """
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo_link = photo_link
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_prior = email_prior
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.address_secondary = address_secondary
        self.phone_secondary = phone_secondary
        self.notes = notes






