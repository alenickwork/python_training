__author__ = "Elena Dimchenko"

import random

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
                 notes = None
                 ):
        local_vars=locals()
        for r_arg in filter(lambda _: local_vars[_] == "random", local_vars.keys()):
            if r_arg in ["anniversary_day", "birthday_day"]:
                self.__dict__[r_arg] = str(random.randint(1,28))
                continue
            if r_arg in ["anniversary_month", "birthday_month"]:
                self.__dict__[r_arg] = "August"
                continue
            if r_arg in ["anniversary_year", "birthday_year"]:
                self.__dict__[r_arg] = str(random.randint(1900, 2017))
                continue
            self.__dict__[r_arg] = str(random.randint(100000, 999999))

        for r_arg in filter(lambda _: local_vars[_] != "random", local_vars.keys()):
           self.__dict__[r_arg] = local_vars[r_arg]

    def dummy(self):
        print("Creating dummy contact data")
        for param in self.__dict__.keys():
            self.__dict__[param] = str(random.randint(100000,999999))
        self.photo_link = None
        self.anniversary_day = str(random.randint(1,28))
        self.anniversary_month = "June"
        self.anniversary_year = str(random.randint(1950,2000))
        self.birthday_day = str(random.randint(1,28))
        self.birthday_month = "April"
        self.birthday_year = str(random.randint(1950,2000))

    @property
    def xpath(self):
        return xpath_records(self)


class xpath_records:
    def __init__(self, cont):
        self.row = ".//table[@id='maintable']/descendant::tr[@name='entry']/descendant::td[text()='{last_name}']/following-sibling::td[text()='{first_name}']".format(last_name = cont.lastname, first_name = cont.firstname)
        self.checkbox = self.row+"/preceding-sibling::td[@class='center']/input[@type='checkbox']"
        self.edit = self.row+"/following-sibling::td[@class ='center']/a[contains(@href,'edit')]"





