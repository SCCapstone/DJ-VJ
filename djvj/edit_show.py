"""class for editing parameters"""
import tkinter as tk
from tkinter import filedialog, Button, Label, Entry, \
    OptionMenu, END, Frame, Listbox, Toplevel, StringVar, Scrollbar, messagebox
import os
import pickle
import time

final_rules = {}


class EditShow(tk.Tk):
    """TODO description"""


    def __init__(self, master, rule_dictionary):
        self.final_rules = rule_dictionary
        top = self.top = master
        frame = Frame(top)
        frame.pack()
        Label(frame, text="Edit Show").grid(row=0, column=0, rowspan=1, columnspan=2)
        self.charbox = Listbox(frame, width=100)
        for chars in []:
            self.charbox.insert(END, chars)
        self.charbox.grid(row=1, column=0, rowspan=5)
        Label(frame, text="Add New Rule").grid(row=6, column=0)
        new_rule_frame = Frame(frame, height=100, width=100, borderwidth=2)
        new_rule_frame.grid(column=0, row=7, columnspan=2)

        Label(new_rule_frame, text="Select Moment: ").grid(row=0, column=0, rowspan=1, columnspan=1)

        self.mom_val = StringVar(top)
        self.mom_val.set(".....")  # default value
        self.set_attribute = OptionMenu(
            new_rule_frame, self.mom_val, *rule_dictionary.keys()).grid(row=0, column=1, rowspan=1, columnspan=1)

        Label(new_rule_frame, text="              ").grid(row=0, column=2, rowspan=1, columnspan=1)
        
        Label(new_rule_frame, text="If   ").grid(row=0, column=3, rowspan=1, columnspan=1)

        self.attr_val = StringVar(top)
        self.attr_val.set(".....")  # default value
        self.set_attribute = OptionMenu(
            new_rule_frame, self.attr_val , "pitch", "tempo", "time").grid(row=0, column=4, rowspan=1, columnspan=1)

        self.sign_val = StringVar(top)
        self.sign_val.set(".....")  # default value
        self.set_sign = OptionMenu(
            new_rule_frame, self.sign_val , ">", "<", "=").grid(row=0, column=5, rowspan=1, columnspan=1)

        self.target_val = Entry(new_rule_frame, width=10)
        self.target_val.grid(row=0, column=6, rowspan=1, columnspan=1)

        Label(new_rule_frame, text="   play   ").grid(row=0, column=7, rowspan=1, columnspan=1)

        Button(new_rule_frame, text="Choose Video", command=self.choose_video).grid(row=0, column=8)

        self.vid_scroll = Scrollbar(new_rule_frame, orient="horizontal")
        self.vid_scroll.grid(row=1, column=9)

        self.vid_label = StringVar(top)
        self.vid_label.set("...")
        self.vid_entry = Entry(new_rule_frame, textvariable=self.vid_label, state='disabled',
                               xscrollcommand=self.vid_scroll.set)
        self.vid_entry.grid(row=0, column=9, rowspan=1, columnspan=1)
        self.vid_scroll.config(command=self.vid_entry.xview)

        self.load_list_params()

        Button(new_rule_frame, text="   Add   ", command=self.add_param).grid(row=0, column=10)
        Button(new_rule_frame, text="   Clear   ", command=self.clear_add).grid(row=1, column=10)

        Button(frame, text="Remove", command=self.remove_param).grid(row=2, column=1)
        Button(frame, text="    Edit    ", command=self.edit_param).grid(row=3, column=1)
        Button(frame, text=" Save ", command=self.save_changes) \
            .grid(row=4, column=1)
        Button(frame, text="    Exit    ", command=self.exit_editor).grid(row=5, column=1)

    def exit_editor(self):
        global final_rules
        self.final_rules.clear()
        self.top.destroy()

    def choose_video(self):
        video_path = filedialog.askopenfilename(initialdir="/home/Documents",
                                                title="Select video for current moment",
                                                filetypes=(("mov files", "*.MOV"),
                                                           ("mp4 files", "*.mp4"),
                                                           ("all files", "*.*")))
        # path, file = os.path.split(video_path)
        self.vid_entry.config(state="normal")
        self.vid_label.set(video_path)
        self.vid_entry.config(textvariable=self.vid_label)
        self.vid_entry.config(state="disabled")

    def load_list_params(self):
        self.charbox.delete(0, END)
        global final_rules
        list_dict = self.final_rules
        for i in list_dict.keys():
            self.charbox.insert(END, i)
            for x in list_dict[i]:
                self.charbox.insert(END, x)

    def clear_add(self):

        self.vid_entry.config(state="normal")
        self.vid_label.set("...")
        self.vid_entry.config(textvariable=self.vid_label)
        self.vid_entry.config(state="disabled")

        self.mom_val.set(".....")
        self.attr_val.set(".....")
        self.sign_val.set(".....")
        self.target_val.delete(0, "end")

    def add_param(self):
        # TODO description
        global final_rules
        add_rule = True
        invalid_string = ""
        current_moment = self.mom_val.get()
        new_attr = self.attr_val.get()
        new_sign = self.sign_val.get()
        new_tval = self.target_val.get()
        new_vid = self.vid_entry.get()

        new_list = list()
        if current_moment == ".....":
            print("MOMENT FALSE")
            invalid_string += ("Invalid moment. " + '\n')
            add_rule = False
        else:
            print("MOMENT TRUE")

        if new_attr in ('pitch', 'tempo', 'time'):
            print("ATTR TRUE")
            new_list.append(new_attr)
        else:
            print("ATTR FALSE")
            invalid_string += ("Invalid attribute. " + '\n')
            add_rule = False

        if new_sign in ('>', '<', '='):
            print("SIGN TRUE")
            new_list.append(new_sign)
        else:
            print("SIGN FALSE")
            invalid_string += ("Invalid sign. " + '\n')
            add_rule = False

        if new_tval is not '' and int(new_tval) > 0:
                print("TVAL TRUE")
                new_list.append(new_tval)
        else:
            print("TVAL FALSE")
            invalid_string += ("Invalid target value. " + '\n')
            add_rule = False

        if new_vid != "..." and os.path.exists(new_vid):
            print("VID PATH TRUE")
            new_list.append(new_vid)
        else:
            print("VID PATH FALSE")
            invalid_string += ("Invalid video path. " + '\n')
            add_rule = False

        if add_rule == True:
            print("new rule added")
            self.final_rules[current_moment].append(new_list)
            new_list.clear()
            self.load_list_params()

        if add_rule == False:
            messagebox.showerror("ERROR", "Please fix the following" + '\n' + invalid_string)
        print(self.final_rules)

    def remove_param(self):
        # TODO description
        global final_rules

        x = self.charbox.curselection()
        y = self.charbox.get(x)
        self.charbox.delete(x)

        target_key = ""
        target_value = ""
        target_value_index = ""

        for key, value in self.final_rules.items():
            for z in range(len(value)):
                if (y[0]) in (value[z]) and \
                        (y[1]) in (value[z]) and \
                        (y[2]) in (value[z]) and \
                        (y[3]) in (value[z]):
                    print("TRUE")
                    target_key = key
                    target_value = value[z]
                    target_value_index = z

        print(".............")
        print(self.final_rules[target_key])
        print("TARGET VALUE INDEX: ")
        print(target_value_index)
        print("TARGET KEY: ")
        print(target_key)
        print("TARGET VALUE: ")
        print(target_value)

        print("List before deletion: ")
        print(self.final_rules[target_key])

        print("List after deletion: ")
        del self.final_rules[target_key][target_value_index]
        print(self.final_rules[target_key])

    def edit_param(self):
        # TODO edit parameter in moment, update dict with new values
        global final_rules
        x = self.charbox.curselection()
        y = self.charbox.get(x)
        print()

    def save_changes(self):
        # TODO fix this
        # TODO description
        global final_rules
        rules = ""
        for key, value in self.final_rules.items():
            vid = (" Moment -- Video: " + str(value[0][3]))
            mom = vid + "\n"
            for x in range(len(value)):
                r = ("If\t" + str(value[x][0]) + "\t" + str(value[x][1]) +
                     "\t" + str(value[x][2]) + "\t play\t" + str(value[x][3]))
                rs = r + "\n"
            concat = mom + rs
            rules += concat
        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location",
                                                filetypes=(("djvj files", "*.djvj"),
                                                           ("all files", "*.*")))
        if filename != "":
            # adds to file
            pickle.dump(rules, open("%s.djvj" % filename, "wb"))
            time.sleep(2)

