from model.group import Group
from .helpers.base_list import BaseList

class GroupsList(BaseList):
    def __init__(self,app):
        super(GroupsList, self).__init__(app)
        self.members = self.app.group.get_group_list()
        self.key = Group.id_or_max
        #self.normalize()
    def __eq__(self, other):
        return self.normalized == other.normalized

    @property
    def members_number(self):
        return self.app.group.count