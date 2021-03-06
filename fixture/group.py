from fixture.actions import ActionsHelper

from model.group import Group

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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_by_index(0)

    def delete_by_index(self, index = 0):
        print("Delete group # {0}".format(index))
        self.open_groups_page()
        self.select_group_by_index(index)
        self.input_click("Delete group(s)")
        self.return_to_groups_page()
        self.group_cache = None


    def delete_by_id(self, id = 0):
        print("Delete group # {0}".format(id))
        self.open_groups_page()
        self.select_group_by_id(id)
        self.input_click("Delete group(s)")
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        el = wd.find_element_by_css_selector("input[value='%s']" % id)
        el.click()
        return el

    def select_group_by_index(self, index):
        wd = self.app.wd
        el = wd.find_elements_by_name("selected[]")[index]
        el.click()
        return el


    def delete(self, group_data):
        print("Delete group {0}".format(group_data.name))
        self.open_groups_page()
        to_del = self.app.wd.find_element_by_xpath(group_data.xpath.checkbox)
        if not to_del.is_selected():
            to_del.click()
        self.input_click("Delete group(s)")
        self.return_to_groups_page()
        self.group_cache = None

    def modify(self, group_data, new_group_data):
        print("Modify group {0}".format(group_data.name))
        self.open_groups_page()
        to_mod = self.app.wd.find_element_by_xpath(group_data.xpath.checkbox)
        if not to_mod.is_selected():
            to_mod.click()
        self.input_click("Edit group")
        self._enter_data(new_group_data)
        self.update()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first(self, new_group_data):
        self.modify_by_index(0,new_group_data)

    def modify_by_id(self, id, new_group_data):
        wd = self.app.wd
        print("Modify group #{0}".format(id))
        self.open_groups_page()
        self.select_group_by_id(id)
        self.input_click("Edit group")
        self._enter_data(new_group_data)
        self.update()
        self.return_to_groups_page()
        self.group_cache = None



    def modify_by_index(self, index, new_group_data):
        wd = self.app.wd
        print("Modify group #{0}".format(index))
        self.open_groups_page()
        self.select_group_by_index(index)
        self.input_click("Edit group")
        self._enter_data(new_group_data)
        self.update()
        self.return_to_groups_page()
        self.group_cache = None

    @property
    def count(self):
       wd = self.app.wd
       self.open_groups_page()
       tmp = len(wd.find_elements_by_name("selected[]"))
       print("{0} Groups found".format(tmp))
       return tmp

    @property
    def page_is_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0

    def open_groups_page(self):
        if not self.page_is_opened:
            print("Open groups page")
            self.link_click("groups")
            self.wait_button_clickable("New group")


    def return_to_groups_page(self):
        self.open_groups_page()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache)

    def _click_new(self):
        print("Click new group")
        self.button_click("new")
        self.wait_button_clickable("Enter information")

    def _enter_data(self, group_data):
        print("Enter group data")
        if group_data.name is not None:
            self.text_input(field_name="group_name", value=group_data.name)
        if group_data.header is not None:
            self.text_input(field_name="group_header", value=group_data.header)
        if group_data.footer is not None:
            self.text_input(field_name="group_footer", value=group_data.footer)


