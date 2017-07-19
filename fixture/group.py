from fixture.actions import ActionsHelper

class GroupHelper(ActionsHelper):
    def __init__(self,app):
        super(GroupHelper,self).__init__(app)
        self.app = app

    def create(self, group_data):
        print("Create new group")
        self.open_groups_page()
        self._click_new()
        self._enter_data(group_data)
        self.submit()
        self.return_to_groups_page()

    def delete_first_group(self):
        print("Delete 1st group")
        self.open_groups_page()
        self.menu_item_click("selected[]")
        self.input_click("Delete group(s)")
        self.return_to_groups_page()

    def delete(self, group_data):
        print("Delete group {0}".format(group_data.name))
        self.open_groups_page()
        to_del = self.app.wd.find_element_by_xpath(group_data.xpath.checkbox)
        if to_del is None:
            return None

        if not to_del.is_selected():
            to_del.click()
        self.input_click("Delete group(s)")
        self.return_to_groups_page()

    def modify(self, group_data, new_group_data):
        print("Modify group {0}".format(group_data.name))
        self.open_groups_page()
        to_mod = self.app.wd.find_element_by_xpath(group_data.xpath.checkbox)
        if to_mod is None:
            return None
        if not to_mod.is_selected():
            to_mod.click()
        self.input_click("Edit group")
        self._enter_data(new_group_data)
        self.update()
        self.return_to_groups_page()

    def open_groups_page(self):
        print("Open groups page")
        self.link_click("groups")

    def return_to_groups_page(self):
        self.open_groups_page()

    def _click_new(self):
        print("Click new group")
        self.button_click("new")

    def _enter_data(self, group_data):
        print("Enter group data")
        if group_data.name is not None:
            self.text_input(field_name="group_name", value=group_data.name)
        if group_data.header is not None:
            self.text_input(field_name="group_header", value=group_data.header)
        if group_data.footer is not None:
            self.text_input(field_name="group_footer", value=group_data.footer)


