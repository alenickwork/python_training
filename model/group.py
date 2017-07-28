__author__ = "Elena Dimchenko"

from .helpers.randomize import randomize_it
from sys import maxsize

class Group:

    def __init__(self,
                 name = None,
                 id = None,
                 header = None,
                 footer = None
                 ):
        self.name = randomize_it(name)
        self.id = id
        self.header = randomize_it(header)
        self.footer = randomize_it(footer)
        print(self.__repr__())


    def dummy(self):
        print("Creating dummy group data")
        self.name = randomize_it("random")
        self.header = randomize_it("random")
        self.footer = randomize_it("random")

    @property
    def xpath(self):
        return xpath_records(self)

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class xpath_records:
    def __init__(self, group):
        self.row = ".//span[text() = '{0}']".format(group.name)
        self.checkbox = self.row+"/input[@type = 'checkbox']"
