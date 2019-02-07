#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 11, 2019 12:32:59 PM EST  platform: Windows NT

import sys
from src.Fridge import Fridge
from src.Alcoholic import Alcoholic
from src.Glass import Glass
from src.Inventory import Inventory


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class PyDrinkController:

    def __init__(self):
        self._fridge = Fridge()
        self._glass = Glass()
        self._inventory = Inventory()

    @property
    def fridge(self):
        return self._fridge

    @fridge.setter
    def fridge(self, value):
        self._fridge = value

    @property
    def glass(self):
        return self._glass

    @glass.setter
    def glass(self, value):
        self._glass = value

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value

    def search(self, text, prev, next, inventory_list, textbox_selected, success_message, page_message):
        print('PyDrink_support.search: %s' % text)
        if text == "":
            text = None

        self.inventory.page = 1
        self.inventory.search_params = text

        self.inventory.get_products(text)
        PyDrinkController.insert_manager_tree(inventory_list, textbox_selected, self.inventory, "Added To Cart",
                                              success_message)

        if self.inventory.page == 1:
            prev.configure(state=tk.DISABLED)
        if self.inventory.final_page:
            next.configure(state=tk.DISABLED)

        text = "Page %g of %g" % (self.inventory.page, self.inventory.num_pages)
        page_message.configure(text=text)

        sys.stdout.flush()

    @staticmethod
    def btn_add_glass_lclick(p1, tree, glass_list, selection_message, success_message):
        print('PyDrink_support.btn_add_glass_lclick')
        print('p1 = {0}'.format(p1))

        """Event triggered when add to glass button is pressed
        1. Empties the Glass TreeView in Glass tab
        2. Repopulates it with all selected Beverages in the Fridge tab"""
        try:
            for child in glass_list.get_children():
                glass_list.delete(child)

            # Iterate through all items in TreeView adding all selected items to Glass
            count = 0
            for child in tree.get_children():
                if tree.item(child, "values")[0] == selection_message:
                    count += 1
                    glass_list.insert('', 'end', text=tree.item(child, "text"), values=tree.item(child, "values"))

            if count > 0:
                success_message.configure(state=tk.NORMAL)
        except:
            pass
        sys.stdout.flush()

    def btn_add_fridge_lclick(self, inventory_list, success_message, page_message, selection_message):
        print('PyDrink_support.btn_add_fridge_lclick')
        """Event triggered when add to fridge button is pressed
            1. Adds selected drinks to the fridge tab"""
        try:
            count = 0
            for child in inventory_list.get_children():
                if inventory_list.item(child, "values")[0] == selection_message and not self.fridge.find_drink('name',
                       inventory_list.item(child, "text")):
                    print("Adding %s" % inventory_list.item(child, "text"))
                    count += 1
                    d = self.inventory.find_drink('name', inventory_list.item(child, "text"))
                    d.selected = False
                    self.fridge.add_drink(d)
                    self.fridge.save()

            if count > 0:
                success_message.configure(state=tk.NORMAL)

            text = "Page %g of %g" % (self.inventory.page, self.inventory.num_pages)
            page_message.configure(text=text)

            sys.stdout.flush()
        except:
            pass

    def btn_remove_fridge_lclick(self, tree, description):
        print('PyDrink_support.btn_remove_fridge_lclick')
        """Event triggered when remove from fridge button is pressed
                1. Remove selected drinks to the fridge tab"""
        try:
            item = tree.selection()[0]
            drink = self.fridge.find_drink('name', tree.item(item, "text"))
        except IndexError:
            drink = None
            pass

        if drink is not None:
            tree.delete(item)
            self.fridge.remove_drink(drink.id)
            description.delete('1.0', tk.END)
            self.fridge.save()

        sys.stdout.flush()

    def btn_inv_prev_lclick(self, prev, next, inventory_list, textbox_selected, success_message, page_message):
        print('PyDrink_support.btn_inv_prev_lclick')

        """Event triggered when prev button is pressed
        1. Empties the Inventory TreeView in Inventory tab
        2. Repopulates it with previous page"""
        for child in inventory_list.get_children():
            inventory_list.delete(child)

        self.inventory.page -= 1
        next.configure(state=tk.NORMAL)

        self.inventory.get_products(self.inventory.search_params)
        PyDrinkController.insert_manager_tree(inventory_list, textbox_selected, self.inventory, "Added To Cart",
                                              success_message)

        if self.inventory.page == 1:
            prev.configure(state=tk.DISABLED)

        text = "Page %g of %g" % (self.inventory.page, self.inventory.num_pages)
        page_message.configure(text=text)

        sys.stdout.flush()

    def btn_inv_next_lclick(self, prev, next, inventory_list, textbox_selected, success_message, page_message):
        print('PyDrink_support.btn_inv_next_lclick')

        """Event triggered when prev button is pressed
        1. Empties the Inventory TreeView in Inventory tab
        2. Repopulates it with previous page"""
        for child in inventory_list.get_children():
            inventory_list.delete(child)

        self.inventory.page += 1
        prev.configure(state=tk.NORMAL)

        self.inventory.get_products(self.inventory.search_params)
        PyDrinkController.insert_manager_tree(inventory_list, textbox_selected, self.inventory, "Added To Cart",
                                              success_message)

        if self.inventory.final_page:
            next.configure(state=tk.DISABLED)

        text = "Page %g of %g" % (self.inventory.page, self.inventory.num_pages)
        page_message.configure(text=text)

        sys.stdout.flush()

    def ntb_open_inventory(self, p1, tree, textbox_selected, success_message, page_message):
        print('PyDrink_support.ntb_open_inventory')
        print('p1 = {0}'.format(p1))

        """Event triggered when the inventory tab is opened
            Call method to add drinks from the API to the TreeView"""

        PyDrinkController.insert_manager_tree(tree, textbox_selected,  self.inventory, "Added To Cart",
                                              success_message)
        text = "Page %g of %g" % (self.inventory.page, self.inventory.num_pages)
        page_message.configure(text=text)
        sys.stdout.flush()

    def ntb_open_fridge(self, p1, tree, textbox_selected, success_message):
        print('PyDrink_support.ntb_open_fridge')
        print('p1 = {0}'.format(p1))

        """Event triggered when the fridge tab is opened
        Call method to add drinks from the fridge to the TreeView"""

        success_message.configure(state=tk.DISABLED)
        PyDrinkController.insert_manager_tree(tree, textbox_selected, self.fridge, "Added To Glass", success_message)

        sys.stdout.flush()

    def ntb_open_glass(self, p1, tree, cocktail_tree, textbox_selected):
        print('PyDrink_support.ntb_open_glass')
        print('p1 = {0}'.format(p1))

        """Event triggered when the Glass tab is opened
            Call method to add drinks from the glass object to the TreeView,
            Call method to add cocktails to the TreeView"""

        cocktail_categories = {}
        alcoholic = []
        non_alcoholic = []

        """Iterate through all items in TreeView adding all to dict obj"""
        self.glass.clear_drinks()
        for child in tree.get_children():
            drink = self.fridge.find_drink('name', tree.item(child, "text"))
            if not self.glass.has_drink(drink.id):
                self.glass.add_drink(drink)
            if isinstance(drink, Alcoholic):
                alcoholic.append(drink.category)
            else:
                non_alcoholic.append(drink.desc)

        cocktail_categories["Alcoholic"] = alcoholic
        cocktail_categories["NonAlcoholic"] = non_alcoholic
        PyDrinkController.insert_cocktail_tree(cocktail_tree, self.glass, cocktail_categories, textbox_selected)

        sys.stdout.flush()

    @staticmethod
    def init(top, gui, *args, **kwargs):
        global w, top_level, root
        w = gui
        top_level = top
        root = top

    @staticmethod
    def destroy_window():
        # Function which closes the window.
        global top_level
        top_level.destroy()
        top_level = None

    @staticmethod
    def insert_manager_tree(tree, textbox_selected, obj, selection_message, success_message=None):
        """Insertion method."""
        # Clears TreeView
        for child in tree.get_children():
            tree.delete(child)

        for drink in obj.drinks.values():
            selected = ('', '')
            if drink.selected:
                selected = (selection_message, '')

            tree.insert('', 'end', text=str(drink.name), values=selected)
            tree.bind("<ButtonRelease-3>", lambda e: PyDrinkController.stv_list_selected_rclick(e, tree, obj,
                                                                                                selection_message,
                                                                                                success_message))
            tree.bind("<ButtonRelease-1>", lambda e: PyDrinkController.stv_select_lclick(e, tree, obj,
                                                                                         textbox_selected))

    @staticmethod
    def insert_cocktail_tree(tree, obj, categories, textbox_selected):
        """Insertion method."""
        # Clears TreeView
        for child in tree.get_children():
            tree.delete(child)

        for cocktail in obj.find_cocktails(categories):
            tree.insert('', 'end', text=str(cocktail.name),
                        values='No')
            tree.bind("<ButtonRelease-1>", lambda e: PyDrinkController.stv_cocktail_selected(e, tree, obj,
                                                                                             textbox_selected))

    @staticmethod
    def stv_select_lclick(p1, tree, obj, textbox_selected):
        """Update Description of selected frame"""
        print('PyDrink_support.stv_list_selected_lclick')
        print('p1 = {0}'.format(p1))

        try:
            item = tree.selection()[0]
            drink = obj.find_drink('name', tree.item(item, "text"))
        except IndexError:
            drink = None
            pass

        if drink is not None:
            # 1 - line 0 - coloumn
            textbox_selected.delete('1.0', tk.END)
            textbox_selected.insert('1.0', str(drink))

    @staticmethod
    def stv_cocktail_selected(p1, tree, obj, textbox_selected):
        """Update Description of selected frame"""
        print('PyDrink_support.stv_cocktail_selected')
        print('p1 = {0}'.format(p1))
        try:
            item = tree.selection()[0]
            cocktail = obj.get_cocktail(tree.item(item, "text"))
        except IndexError:
            cocktail = None
            pass

        if cocktail is not None:
            # 1 - line 0 - coloumn
            textbox_selected.delete('1.0', tk.END)
            textbox_selected.insert('1.0', str(cocktail))

    @staticmethod
    def stv_list_selected_rclick(p1, tree, obj, selection_message, success_message):
        """Update Selection of drink in fridge"""
        print('PyDrink_support.stv_list_selected_rclick')
        print('p1 = {0}'.format(p1))
        sys.stdout.flush()
        try:
            item = tree.selection()[0]
            drink = obj.find_drink('name', tree.item(item, "text"))

            # Flip sign of selected
            if tree.item(item, "values")[0] == '':
                tree.item(item, values=(selection_message, ""))
                drink.selected = True
            else:
                tree.item(item, values=('', ''))
                drink.selected = False

            if success_message is not None:
                success_message.configure(state=tk.DISABLED)

            if type(obj) is Fridge:
                obj.save()
        except:
            pass

        sys.stdout.flush()


if __name__ == '__main__':
    import PyDrink
    PyDrink.vp_start_gui()



