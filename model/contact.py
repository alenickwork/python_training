__author__ = "Elena Dimchenko"

import random
from .helpers.randomize import randomize_it
from sys import maxsize

class Contact:
    def __init__(self, firstname = None,
                 middlename = None,
                 lastname = None,
                 nickname = None,
                 photo_link = None,
                 title = None,
                 company = None,
                 address = None,
                 home_phone = None,
                 mobile_phone = None,
                 work_phone = None,
                 fax = None,
                 email_prior = None,
                 email_2 = None,
                 email_3 = None,
                 homepage = None,
                 birthday_day = None,
                 birthday_month = None,
                 birthday_year = None,
                 anniversary_day = None,
                 anniversary_month = None,
                 anniversary_year = None,
                 address_secondary = None,
                 phone_secondary = None,
                 notes = None,
                 id = None
                 ):
        local_vars=locals()
        self.firstname = randomize_it(firstname)
        self.middlename = randomize_it(middlename)
        self.lastname = randomize_it(lastname)
        self.nickname = randomize_it(nickname)
        self.photo_link = randomize_it(photo_link)
        self.title = randomize_it(title)
        self.company = randomize_it(company)
        self.address = randomize_it(address)
        self.home_phone = randomize_it(home_phone)
        self.mobile_phone = randomize_it(mobile_phone)
        self.work_phone = randomize_it(work_phone)
        self.fax = randomize_it(fax)
        self.email_prior = randomize_it(email_prior)
        self.email_2 = randomize_it(email_2)
        self.email_3 = randomize_it(email_3)
        self.homepage = randomize_it(homepage)
        self.birthday_day = randomize_it(birthday_day,"day_of_month")
        self.birthday_month = randomize_it(birthday_month,"month")
        self.birthday_year = randomize_it(birthday_year,"year")
        self.anniversary_day = randomize_it(anniversary_day,"day_of_month")
        self.anniversary_month = randomize_it(anniversary_month,"month")
        self.anniversary_year = randomize_it(anniversary_year,"year")
        self.address_secondary = randomize_it(address_secondary)
        self.phone_secondary = randomize_it(phone_secondary)
        self.notes = randomize_it(notes)
        self.id = id
        print(self.__repr__())

    def dummy(self):
        print("Creating dummy contact data")
        self.firstname = randomize_it("random")
        self.middlename = randomize_it("random")
        self.lastname = randomize_it("random")
        self.nickname = randomize_it("random")
        self.photo_link = None
        self.title = randomize_it("random")
        self.company = randomize_it("random")
        self.address = randomize_it("random")
        self.home_phone = randomize_it("random")
        self.mobile_phone = randomize_it("random")
        self.work_phone = randomize_it("random")
        self.fax = randomize_it("random")
        self.email_prior = randomize_it("random")
        self.email_2 = randomize_it("random")
        self.email_3 = randomize_it("random")
        self.homepage = randomize_it("random")
        self.birthday_day = randomize_it("random","day_of_month")
        self.birthday_month = randomize_it("random","month")
        self.birthday_year = randomize_it("random","year")
        self.anniversary_day = randomize_it("random","day_of_month")
        self.anniversary_month = randomize_it("random","month")
        self.anniversary_year = randomize_it("random","year")
        self.address_secondary = randomize_it("random")
        self.phone_secondary = randomize_it("random")
        self.notes = randomize_it("random")
        self.id = None

    @property
    def xpath(self):
        return xpath_records(self)

    def __repr__(self):
        return "%s : %s.%s" %(self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        print("---------")
        print(self.__repr__())
        print(other.__repr__())
        print (self.firstname is None or other.firstname is None or self.firstname == other.firstname)
        print (self.lastname is None or other.lastname is None or self.lastname == other.lastname)
        print (self.id is None or other.id is None or self.id == other.id)
        return (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)\
               and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id is not None:
            return int(self.id)
        else:
            return maxsize

class xpath_records:
    def __init__(self, cont):
        self.row = ".//table[@id='maintable']/descendant::tr[@name='entry']/descendant::td[text()='{last_name}']/following-sibling::td[text()='{first_name}']".format(last_name = cont.lastname, first_name = cont.firstname)
        self.checkbox = self.row+"/preceding-sibling::td[@class='center']/input[@type='checkbox']"
        self.edit = self.row+"/following-sibling::td[@class ='center']/a[contains(@href,'edit')]"





