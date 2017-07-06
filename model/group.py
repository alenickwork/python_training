__author__ = "Elena Dimchenko"

import random

class Group:

    def __init__(self,
                 name = None,
                 header = None,
                 footer = None):
        local_vars=locals()
        for r_arg in filter(lambda _: local_vars[_] == "random", local_vars.keys()):
            self.__dict__[r_arg] = str(random.randint(100000, 999999))
        for r_arg in filter(lambda _: local_vars[_] != "random", local_vars.keys()):
           self.__dict__[r_arg] = local_vars[r_arg]

    def dummy(self):
        print("Creating dummy group data")
        for param in self.__dict__.keys():
            self.__dict__[param] = str(random.randint(100000,999999))

    @property
    def xpath(self):
        return xpath_records(self)


class xpath_records:
    def __init__(self, group):
        self.row = ".//span[text() = '{0}']".format(group.name)
        self.checkbox = self.row+"/input[@type = 'checkbox']"
