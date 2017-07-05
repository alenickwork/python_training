class GroupHelper:
    def __init__(self,app):
        self.app = app

    def create(self, group_data):
        print("Create new group")
        self.open_groups_page()
        self._click_new()
        self._enter_data(group_data)
        self.app.page_objects.submit()
        self.open_groups_page()

    def open_groups_page(self):
        print("Open groups page")
        self.app.page_objects.link_click("groups")

    def _click_new(self):
        print("Click new group")
        self.app.page_objects.button_click("new")

    def _enter_data(self, group_data):
        print("Enter group data")
        self.app.page_objects.text_input(field_name="group_name", value=group_data.name)
        self.app.page_objects.text_input(field_name="group_header", value=group_data.header)
        self.app.page_objects.text_input(field_name="group_footer", value=group_data.footer)
