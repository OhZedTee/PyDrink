#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 11, 2019 12:32:53 PM EST  platform: Windows NT

import sys
import platform

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

from src import PyDrink_support
from ui import ScrolledTreeView
from ui import ROText
from ui import SearchBox


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = tk.Tk()
    top = PyDrink(root)
    PyDrink_support.init(root, top)
    root.mainloop()


w = None


def create_PyDrink(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = PyDrink(w)
    PyDrink_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_PyDrink():
    global w
    w.destroy()
    w = None


class PyDrink:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1080x720+225+19")
        top.title("PyDrink")
        top.configure(background="#d9d9d9")

        self.images = (

         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])

        self.style.configure('TNotebook.Tab', background=_bgcolor, foreground=_fgcolor, tabposition="center",
                             width=root.winfo_screenwidth())
        self.style.map('TNotebook.Tab', background=[('selected', _compcolor), ('active', _ana2color)])
        self.notebook = ttk.Notebook(top)
        self.notebook.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.notebook.configure(takefocus="")
        self.notebook_t0 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t0, padding=3)
        self.notebook.tab(0, text="Inventory", compound="none", underline="-1")
        self.notebook_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        self.notebook_t1 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t1, padding=3)
        self.notebook.tab(1, text="Fridge", compound="none", underline="-1")
        self.notebook_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        self.notebook_t2 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t2, padding=3)
        self.notebook.tab(2, text="Glass", compound="none", underline="-1")
        self.notebook_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.cnv_list_inv = tk.Canvas(self.notebook_t0)
        self.cnv_list_inv.place(relx=0.0, rely=0.015, relheight=0.919
                                , relwidth=0.635)
        self.cnv_list_inv.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief='ridge',
                                    selectbackground="#c4c4c4", selectforeground="black", width=683)

        self.frame_list_inv = tk.Frame(self.cnv_list_inv)
        self.frame_list_inv.place(relx=0.015, rely=0.016, relheight=0.972
                                     , relwidth=0.974)
        self.frame_list_inv.configure(relief='groove', borderwidth="2", background="#d9d9d9", width=665)

        self.search_inv = SearchBox.SearchBox(self.frame_list_inv, command=lambda: PyDrink_support.search(
            self.search_inv.get_text(), self.btn_inv_prev, self.btn_inv_next, self.stv_list_inv,
            self.txtbx_inv_selected, self.lbl_add_fridge_success, self.lbl_inv_page),
            placeholder="Search by Category (i.e. Beer, Wine, Vodka, Tequila)", entry_highlightthickness=0,
            entry_width=94)
        self.search_inv.place(relx=0.015, rely=0.016)

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        self.stv_list_inv = ScrolledTreeView.ScrolledTreeView(self.frame_list_inv)
        self.stv_list_inv.place(relx=0.015, rely=0.056, relheight=0.90, relwidth=0.962)
        self.stv_list_inv.configure(columns="Select")
        self.stv_list_inv.heading("#0", text="Drink", anchor="center")
        self.stv_list_inv.column("#0", width="308", minwidth="20", stretch="1", anchor="w")
        self.stv_list_inv.heading("Select", text="Select", anchor="center")
        self.stv_list_inv.column("Select", width="309", minwidth="20", stretch="1", anchor="center")
        self.notebook_t0.bind('<Visibility>', lambda e: PyDrink_support.ntb_open_inventory(e, self.stv_list_inv,
                                                                                           self.txtbx_inv_selected,
                                                                                           self.lbl_add_fridge_success,
                                                                                           self.lbl_inv_page))

        self.cnv_select_inv = tk.Canvas(self.notebook_t0)
        self.cnv_select_inv.place(relx=0.632, rely=0.015, relheight=0.919
                                  , relwidth=0.365)
        self.cnv_select_inv.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief='ridge'
                                      , selectbackground="#c4c4c4", selectforeground="black", width=393)

        self.frm_select_inv = tk.Frame(self.cnv_select_inv)
        self.frm_select_inv.place(relx=0.025, rely=0.016, relheight=0.972
                                  , relwidth=0.954)
        self.frm_select_inv.configure(relief='groove', borderwidth="2", background="#d9d9d9", width=375)

        self.lbl_inv_description = tk.Label(self.frm_select_inv)
        self.lbl_inv_description.place(relx=0.027, rely=0.016, height=34, width=106)
        self.lbl_inv_description.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9,
                                           foreground="#000000", text='Description:')
        self.lbl_inv_description.pack(side="top")

        self.lbl_add_fridge_success = tk.Label(self.notebook_t0)
        self.lbl_add_fridge_success.place(relx=0.6, rely=0.943, height=33, width=250)
        self.lbl_add_fridge_success.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9,
                                              foreground="#AE3A3A", text='Added To Fridge',
                                              state=tk.DISABLED)

        self.txtbx_inv_selected = ROText.ROText(self.frm_select_inv)
        self.txtbx_inv_selected.place(relx=0.107, rely=0.081, relheight=0.905, relwidth=0.784)
        self.txtbx_inv_selected.configure(background="white", font="TkTextFont", foreground="black",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="#c4c4c4",
                                          selectforeground="black", width=294, wrap='word')

        self.btn_add_fridge = tk.Button(self.notebook_t0, command=lambda: PyDrink_support.btn_add_fridge_lclick(
            self.stv_list_inv, self.lbl_add_fridge_success, self.lbl_inv_page))
        self.btn_add_fridge.place(relx=0.836, rely=0.943, height=33, width=166)
        self.btn_add_fridge.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", pady="0", text='Add To Fridge')

        self.btn_inv_prev = tk.Button(self.frame_list_inv, command=lambda: PyDrink_support.btn_inv_prev_lclick(
            self.btn_inv_prev, self.btn_inv_next, self.stv_list_inv, self.txtbx_inv_selected,
            self.lbl_add_fridge_success, self.lbl_inv_page))
        self.btn_inv_prev.place(relx=0.25, rely=0.96, height=22, width=18)
        self.btn_inv_prev.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='<', state='disabled')
        self.lbl_inv_page = tk.Label(self.frame_list_inv)
        self.lbl_inv_page.place(relx=0.5, rely=0.973, height=22, width=125, anchor="center")
        self.lbl_inv_page.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9,
                                    foreground="#000000", text='')

        self.btn_inv_next = tk.Button(self.frame_list_inv, command=lambda: PyDrink_support.btn_inv_next_lclick(
            self.btn_inv_prev, self.btn_inv_next, self.stv_list_inv, self.txtbx_inv_selected,
            self.lbl_add_fridge_success, self.lbl_inv_page))
        self.btn_inv_next.place(relx=0.75, rely=0.96, height=22, width=18)
        self.btn_inv_next.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='>')

        self.cnv_list_fridge = tk.Canvas(self.notebook_t1)
        self.cnv_list_fridge.place(relx=0.0, rely=0.015, relheight=0.919
                                   , relwidth=0.635)
        self.cnv_list_fridge.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief='ridge',
                                       selectbackground="#c4c4c4", selectforeground="black", width=683)

        self.frame_list_fridge = tk.Frame(self.cnv_list_fridge)
        self.frame_list_fridge.place(relx=0.015, rely=0.016, relheight=0.972
                                     , relwidth=0.974)
        self.frame_list_fridge.configure(relief='groove', borderwidth="2", background="#d9d9d9", width=665)

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.stv_list_fridge = ScrolledTreeView.ScrolledTreeView(self.frame_list_fridge)
        self.stv_list_fridge.place(relx=0.015, rely=0.016, relheight=0.971
                                   , relwidth=0.962)
        self.stv_list_fridge.configure(columns="Select")
        self.stv_list_fridge.heading("#0", text="Drink", anchor="center")
        self.stv_list_fridge.column("#0", width="308", minwidth="20", stretch="1", anchor="w")
        self.stv_list_fridge.heading("Select", text="Select", anchor="center")
        self.stv_list_fridge.column("Select", width="309", minwidth="20", stretch="1", anchor="center")
        self.notebook_t1.bind('<Visibility>', lambda e: PyDrink_support.ntb_open_fridge(e, self.stv_list_fridge,
                                                                                        self.txtbx_fridge_selected,
                                                                                        self.lbl_add_glass_success))

        self.cnv_select_fridge = tk.Canvas(self.notebook_t1)
        self.cnv_select_fridge.place(relx=0.632, rely=0.015, relheight=0.919
                                     , relwidth=0.365)
        self.cnv_select_fridge.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief='ridge'
                                         , selectbackground="#c4c4c4", selectforeground="black", width=393)

        self.frm_select_fridge = tk.Frame(self.cnv_select_fridge)
        self.frm_select_fridge.place(relx=0.025, rely=0.016, relheight=0.972
                                     , relwidth=0.954)
        self.frm_select_fridge.configure(relief='groove', borderwidth="2", background="#d9d9d9", width=375)

        self.lbl_fridge_description = tk.Label(self.frm_select_fridge)
        self.lbl_fridge_description.place(relx=0.027, rely=0.016, height=34, width=106)
        self.lbl_fridge_description.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9,
                                              foreground="#000000", text='Description:')
        self.lbl_fridge_description.pack(side="top")

        self.lbl_add_glass_success = tk.Label(self.notebook_t1)
        self.lbl_add_glass_success.place(relx=0.027, rely=0.943, height=33, width=250)
        self.lbl_add_glass_success.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9,
                                             foreground="#AE3A3A", text='Successfully Added To Glass',
                                             state=tk.DISABLED)

        self.txtbx_fridge_selected = ROText.ROText(self.frm_select_fridge)
        self.txtbx_fridge_selected.place(relx=0.107, rely=0.081, relheight=0.905, relwidth=0.784)
        self.txtbx_fridge_selected.configure(background="white", font="TkTextFont", foreground="black",
                                             highlightbackground="#d9d9d9", highlightcolor="black",
                                             insertbackground="black", selectbackground="#c4c4c4",
                                             selectforeground="black", width=294, wrap='word')

        self.btn_add_glass = tk.Button(self.notebook_t1)
        self.btn_add_glass.place(relx=0.836, rely=0.943, height=33, width=166)
        self.btn_add_glass.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='Add To Glass')
        self.btn_add_glass.bind('<Button-1>', lambda e: PyDrink_support.btn_add_glass_lclick(e, self.stv_list_fridge,
                                                                                             self.stv_list_glass,
                                                                                             self.lbl_add_glass_success)
                                )

        self.btn_remove_fridge = tk.Button(self.notebook_t1, command=lambda: PyDrink_support.btn_remove_fridge_lclick(
            self.stv_list_fridge, self.txtbx_fridge_selected))
        self.btn_remove_fridge.place(relx=0.65, rely=0.943, height=33, width=166)
        self.btn_remove_fridge.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                         disabledforeground="#a3a3a3", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                         text='Remove From Fridge')

        self.cnv_list_glass = tk.Canvas(self.notebook_t2)
        self.cnv_list_glass.place(relx=0.0, rely=0.015, relheight=0.919
                                  , relwidth=0.635)
        self.cnv_list_glass.configure(background="#d9d9d9", borderwidth="2", highlightbackground="#d9d9d9",
                                      highlightcolor="black", insertbackground="black", relief='ridge',
                                      selectbackground="#c4c4c4", selectforeground="black", width=683)

        self.frame_list_glass = tk.Frame(self.cnv_list_glass)
        self.frame_list_glass.place(relx=0.015, rely=0.016, relheight=0.972
                                    , relwidth=0.974)
        self.frame_list_glass.configure(relief='groove', borderwidth="2", background="#d9d9d9",
                                        highlightbackground="#d9d9d9", highlightcolor="black", width=665)

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        style = ttk.Style(self.style)
        # Commented out lines below left to show what attributes of Treeitem were removed
        style.layout("Treeview.Item",
                     [('Treeitem.padding', {'sticky': 'nswe', 'children':
                         [('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
                          ('Treeitem.image', {'side': 'left', 'sticky': ''}),
                          # ('Treeitem.focus', {'side': 'left', 'sticky': '', 'children': [
                          ('Treeitem.text', {'side': 'left', 'sticky': ''}),
                          # ]})
                          ],
                                            })]
                     )
        self.stv_list_glass = ScrolledTreeView.ScrolledTreeView(self.frame_list_glass)
        self.stv_list_glass.place(relx=0.015, rely=0.016, relheight=0.486
                                  , relwidth=0.962)
        self.stv_list_glass.heading("#0", text="Drink", anchor="center")
        self.stv_list_glass.column("#0", width="308", minwidth="20", stretch="1", anchor="w")
        self.stv_list_glass.configure(style='nodotbox.Treeview', selectmode='none')
        self.notebook_t2.bind('<Visibility>', lambda e: PyDrink_support.ntb_open_glass(e, self.stv_list_glass,
                                                                                       self.stv_list_cocktails,
                                                                                       self.txtbx_glass_selected))

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        self.stv_list_cocktails = ScrolledTreeView.ScrolledTreeView(self.frame_list_glass)
        self.stv_list_cocktails.place(relx=0.015, rely=0.497, relheight=0.485
                                      , relwidth=0.962)
        self.stv_list_cocktails.heading("#0", text="Cocktail", anchor="center")
        self.stv_list_cocktails.column("#0", width="308", minwidth="20", stretch="1", anchor="center")

        self.cnv_select_glass = tk.Canvas(self.notebook_t2)
        self.cnv_select_glass.place(relx=0.632, rely=0.015, relheight=0.919
                                    , relwidth=0.365)
        self.cnv_select_glass.configure(background="#d9d9d9", borderwidth="2", highlightbackground="#d9d9d9",
                                        highlightcolor="black", insertbackground="black", relief='ridge',
                                        selectbackground="#c4c4c4", selectforeground="black", width=393)

        self.frm_select_glass = tk.Frame(self.cnv_select_glass)
        self.frm_select_glass.place(relx=0.025, rely=0.016, relheight=0.972
                                    , relwidth=0.954)
        self.frm_select_glass.configure(relief='groove', borderwidth="2", background="#d9d9d9",
                                        highlightbackground="#d9d9d9", highlightcolor="black", width=375)

        self.lbl_glass_description = tk.Label(self.frm_select_glass)
        self.lbl_glass_description.place(relx=0.027, rely=0.016, height=34, width=294)
        self.lbl_glass_description.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9,
                                             foreground="#000000", text='Ingredients Needed:')
        self.lbl_glass_description.pack(side="top")

        self.txtbx_glass_selected = ROText.ROText(self.frm_select_glass)
        self.txtbx_glass_selected.place(relx=0.107, rely=0.081, relheight=0.905, relwidth=0.784)
        self.txtbx_glass_selected.configure(background="white", font="TkTextFont", foreground="black",
                                            highlightbackground="#d9d9d9", highlightcolor="black",
                                            insertbackground="black", selectbackground="#c4c4c4",
                                            selectforeground="black", width=294, wrap='word')


if __name__ == '__main__':
    vp_start_gui()





