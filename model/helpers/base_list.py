class BaseList:
    def __init__(self,app):
        self.app = app
        self.members = []
        self.key = None

    @property
    def normalized(self):
        return sorted(self.members, key = self.key)

    @property
    def members_number_hashed(self):
        return len(self.members)

    def normalize(self):
        self.members = self.normalized
