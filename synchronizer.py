import subprocess
from tkinter import messagebox
from tkinter.filedialog import *

import pandas as pd
from PIL import Image, ImageTk

import image_compare


class Synchronize:
    def destroy_button_label_comparison(self, which_one, option, path='', new_text=""):
        if option == "keep" and which_one == 1:
            confirm = messagebox.askyesnocancel(title="keep file", message="Do you want to keep the first file?",
                                                default='yes', icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
        elif option == "keep" and which_one == 2:
            confirm = messagebox.askyesnocancel(title="keep file", message="Do you want to keep the second file?",
                                                default='yes', icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass

        elif option == "delete" and path != '' and which_one == 1:
            confirm = messagebox.askyesnocancel(title="delete file", message="Do you want to delete the first file?",
                                                default='yes', icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
            os.remove(path)
        elif option == "delete" and path != '' and which_one == 2:
            confirm = messagebox.askyesnocancel(title="delete file", message="Do you want to delete the second file?",
                                                default='yes', icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
            os.remove(path)

        elif option == "save" and path != '' and which_one == 1:
            confirm = messagebox.askyesnocancel(title="save file", message="Do you want to save the changes in the "
                                                                           "first file?", default='yes',
                                                icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
                with open(path, 'w') as file:
                    file.write(new_text)
                    file.close()
        elif option == "save" and path != '' and which_one == 2:
            confirm = messagebox.askyesnocancel(title="save file", message="Do you want to save the changes of the "
                                                                           "second file?", default='yes',
                                                icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
                with open(path, 'w') as file:
                    file.write(new_text)
                    file.close()

        elif option == "video" and path != '' and which_one == 1:
            confirm = messagebox.askyesnocancel(title="keep video", message="Do you want to keep the first video?",
                                                default='yes',
                                                icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
                try:
                    self.error_label.destroy()
                except:
                    pass
        elif option == "video" and path != '' and which_one == 2:
            confirm = messagebox.askyesnocancel(title="keep video", message="Do you want to keep the second video?",
                                                default='yes',
                                                icon='warning')
            if confirm:
                self.keep_a.destroy()
                self.delete_a.destroy()
                try:
                    self.watch_a.destroy()
                    self.watch_b.destroy()
                except:
                    pass
                try:
                    self.save_b.destroy()
                    self.save_a.destroy()
                except:
                    pass
                try:
                    self.error_label.destroy()
                except:
                    pass
        return 0

    def images(self, path_array, i, j, root):
        hash_array = image_compare.DHash.calculate_hash(path_array[0][i] + path_array[1][i],
                                                        path_array[0][j] + path_array[1][j])
        hamming_distance = image_compare.DHash.hamming_distance(path_array[0][i] + path_array[1][i],
                                                                path_array[0][j] + path_array[1][j])
        if hash_array[0] == hash_array[1] and hamming_distance == 0:
            os.remove(path_array[0][j] + path_array[1][j])
        else:
            image_a = Image.open(path_array[0][i] + path_array[1][i])
            image_b = Image.open(path_array[0][j] + path_array[1][j])
            width_a, height_a = image_a.size
            width_b, height_b = image_b.size
            print(width_b, height_b)

            if width_a > height_a:
                height = width_a / height_a
                height = 300 / height
                image_a = Image.open(path_array[0][i] + path_array[1][i]).resize((int(height), 300),
                                                                                 Image.ANTIALIAS)
                image_a = ImageTk.PhotoImage(image_a)
            elif height_a > width_a:
                width = height_a / width_a
                width = 300 / width
                image_a = Image.open(path_array[0][i] + path_array[1][i]).resize((int(width), 300),
                                                                                 Image.ANTIALIAS)
                image_a = ImageTk.PhotoImage(image_a)
            else:
                image_a = Image.open(path_array[0][i] + path_array[1][i]).resize((300, 300),
                                                                                 Image.ANTIALIAS)
                image_a = ImageTk.PhotoImage(image_a)

            if width_b > height_b:
                height = width_a / height_a
                height = 300 / height
                image_b = Image.open(path_array[0][j] + path_array[1][j]).resize((int(height), 300),
                                                                                 Image.ANTIALIAS)
                image_b = ImageTk.PhotoImage(image_b)
            elif height_b > width_b:
                width = height_a / width_a
                width = 300 / width
                image_b = Image.open(path_array[0][j] + path_array[1][j]).resize((int(width), 300),
                                                                                 Image.ANTIALIAS)
                image_b = ImageTk.PhotoImage(image_b)
            else:
                image_b = Image.open(path_array[0][j] + path_array[1][j]).resize((300, 300),
                                                                                 Image.ANTIALIAS)
                image_b = ImageTk.PhotoImage(image_b)

            self.delete_a = Label(root, image=image_a)
            self.delete_a.place(y=10, x=10)
            self.delete_b = Label(root, image=image_b)
            self.delete_b.place(y=10, x=350)
            self.delete_a = Button(root, text="delete first picture",
                                   command=lambda: self.destroy_button_label_comparison(1, "delete", (
                                           path_array[0][i] + path_array[1][i])))
            self.delete_a.place(y=320, x=10)
            self.delete_b = Button(root, text="delete second picture",
                                   command=lambda: self.destroy_button_label_comparison(2, "delete", (
                                           path_array[0][j] + path_array[1][j])))
            self.delete_b.place(y=320, x=350)
            self.keep_a = Button(root, text="keep first picture",
                                 command=lambda: self.destroy_button_label_comparison(1, "keep"))
            self.keep_a.place(y=320, x=150)
            self.keep_b = Button(root, text="keep second picture",
                                 command=lambda: self.destroy_button_label_comparison(2, "keep"))
            self.keep_b.place(y=320, x=510)
        return 0

    def text_files(self, path_one, path_two, root):
        cant_open = False
        text_one = ""
        text_two = ""

        try:
            with open(path_one, 'r') as file:
                text_one = file.read()
                file.close()
            with open(path_two, 'r') as file:
                text_two = file.read()
                file.close()
        except:
            cant_open = True
            print(path_one, path_two)
            print("can't open")
            pass

        if not cant_open and text_one == text_two:
            os.remove(path_two)
        else:
            scrollbar_y_a = Scrollbar(root)
            scrollbar_y_b = Scrollbar(root)
            scrollbar_x_a = Scrollbar(root)
            scrollbar_x_b = Scrollbar(root)
            text_a = Text(root, height=27.5, width=60)
            text_b = Text(root, height=27.5, width=60)

            scrollbar_y_a.place(x=378, y=10)
            scrollbar_y_b.place(x=768, y=10)
            scrollbar_x_a.place(x=10, y=405)
            scrollbar_x_b.place(x=400, y=405)
            text_a.place(x=10, y=10)
            text_b.place(x=400, y=10)

            scrollbar_y_a.config(command=text_a.yview)
            scrollbar_y_b.config(command=text_b.yview)
            scrollbar_x_a.config(command=text_a.xview)
            scrollbar_x_b.config(command=text_b.xview)
            text_a['yscrollcommand'] = scrollbar_y_a.set
            text_a['xscrollcommand'] = scrollbar_x_a.set
            text_b['yscrollcommand'] = scrollbar_y_b.set
            text_b['xscrollcommand'] = scrollbar_x_b.set
            text_a['font'] = ('Times-Roman', '12')
            text_b['font'] = ('Times-Roman', '12')

            text_a.tag_configure("yellow", background="yellow", font='Times-Roman, 12')
            text_a.tag_configure("white", background="white", font='Times-Roman, 12')
            text_b.tag_configure("yellow", background="yellow", font='Times-Roman, 12')
            text_b.tag_configure("white", background="white", font='Times-Roman, 12')

            item_a = []
            item_b = []

            i = -1
            first_or_empty = True
            last_one_enter = False

            for item in text_one:
                if first_or_empty:
                    item_a.append(item)
                    first_or_empty = False
                    i += 1

                elif item != ' ' and item != '\n' and last_one_enter:
                    item_a.append("")
                    i += 1
                    item_a[i] = item_a[i] + item
                    last_one_enter = False

                elif item != ' ' and item != '\n':
                    item_a[i] = item_a[i] + item

                elif item == ' ' or item == '\n':
                    item_a.append(item)
                    i += 1
                    last_one_enter = True

            i = -1
            first_or_empty = True
            last_one_enter = False

            for item in text_two:
                if first_or_empty:
                    item_b.append(item)
                    first_or_empty = False
                    i += 1

                elif item != ' ' and item != '\n' and last_one_enter:
                    item_b.append("")
                    i += 1
                    item_b[i] = item_b[i] + item
                    last_one_enter = False

                elif item != ' ' and item != '\n':
                    item_b[i] = item_b[i] + item

                elif item == ' ' or item == '\n':
                    item_b.append(item)
                    i += 1
                    last_one_enter = True

            j = 0
            i = 0
            last_color = "white"
            values_i = []

            while True:
                if i >= len(item_a):
                    break
                else:
                    if j < len(item_b):
                        if item_b[j] == ' ' or item_b[j] == '\n':
                            while item_b[j] == ' ' or item_b[j] == '\n':
                                j += 1

                        if item_a[i] == "\n":
                            while item_a[i] == "\n":
                                text_a.insert(END, item_a[i], "white")
                                i += 1

                        elif item_a[i] == " ":
                            if last_color == "white":
                                text_a.insert(END, item_a[i], "white")
                            else:
                                text_a.insert(END, item_a[i], "yellow")
                            i += 1

                        else:
                            if item_a[i] == item_b[j]:
                                text_a.insert(END, item_a[i], "white")
                                last_color = "white"
                            else:
                                text_a.insert(END, item_a[i], "yellow")
                                last_color = "yellow"
                            values_i.append(i)
                            i += 1
                            j += 1

                    else:
                        j = len(item_b) - 1
                        if item_a[i] == "\n":
                            while item_a[i] == "\n":
                                text_a.insert(END, item_a[i], "white")
                                i += 1

                        elif item_a[i] == " ":
                            if last_color == "white":
                                text_a.insert(END, item_a[i], "white")
                            else:
                                text_a.insert(END, item_a[i], "yellow")
                            i += 1

                        else:
                            if item_a[i] == item_b[j]:
                                text_a.insert(END, item_a[i], "white")
                                last_color = "white"
                            else:
                                text_a.insert(END, item_a[i], "yellow")
                                last_color = "yellow"
                            values_i.append(i)
                            i += 1

            j = 0
            k = 0
            last_color = "white"
            while True:
                if j < len(values_i) - 1:
                    i = values_i[k]
                else:
                    i = -1
                if j >= len(item_b):
                    break
                else:
                    if item_b[j] == "\n":
                        while item_b[j] == "\n":
                            text_b.insert(END, item_b[j], "white")
                            j += 1

                    elif item_b[j] == " ":
                        if last_color == "white":
                            text_b.insert(END, item_b[j], "white")
                        else:
                            text_b.insert(END, item_b[j], "yellow")
                        j += 1

                    else:
                        if i != -1:
                            if item_a[i] == item_b[j]:
                                text_b.insert(END, item_b[j], "white")
                                last_color = "white"
                            else:
                                text_b.insert(END, item_b[j], "yellow")
                                last_color = "yellow"
                        else:
                            text_b.insert(END, item_b[j], "yellow")
                            last_color = "yellow"
                        j += 1
                        k += 1

            self.delete_a = Button(root, text="delete first text",
                                   command=lambda: self.destroy_button_label_comparison(1, "delete", path_one))
            self.delete_a.place(y=435, x=10)
            self.delete_b = Button(root, text="delete second text",
                                   command=lambda: self.destroy_button_label_comparison(2, "delete", path_two))
            self.delete_b.place(y=435, x=400)

            self.keep_a = Button(root, text="keep first text",
                                 command=lambda: self.destroy_button_label_comparison(1, "keep"))
            self.keep_a.place(y=435, x=130)
            self.keep_b = Button(root, text="keep second text",
                                 command=lambda: self.destroy_button_label_comparison(2, "keep"))
            self.keep_b.place(y=435, x=540)

            self.save_a = Button(root, text="save first text",
                                 command=lambda: self.destroy_button_label_comparison(1, "save", path_one,
                                                                                      text_a.get("1.0", END)))
            self.save_a.place(y=435, x=240)
            self.save_b = Button(root, text="save second text",
                                 command=lambda: self.destroy_button_label_comparison(2, "save", path_two,
                                                                                      text_b.get("1.0", END)))
            self.save_b.place(y=435, x=670)
        return 0

    @staticmethod
    def open_path_in_explorer(path):
        end_path = r'explorer /select,"'
        temp = ''
        for item in path:
            if item == ' ':
                temp += r'\ '
            else:
                temp += item
        end_path = end_path + temp + '"'
        subprocess.Popen(end_path, shell=True)

    def movies(self, path_one, path_two, root):
        self.delete_a = Button(root, text="delete first video",
                               command=lambda: self.destroy_button_label_comparison(1, "delete", path_one))
        self.delete_a.place(y=435, x=10)
        self.delete_b = Button(root, text="delete second video",
                               command=lambda: self.destroy_button_label_comparison(2, "delete", path_two))
        self.delete_b.place(y=435, x=400)

        self.keep_a = Button(root, text="keep first video",
                             command=lambda: self.destroy_button_label_comparison(1, "video"))
        self.keep_a.place(y=435, x=135)
        self.keep_b = Button(root, text="keep second video",
                             command=lambda: self.destroy_button_label_comparison(2, "video"))
        self.keep_b.place(y=435, x=545)

        self.watch_a = Button(root, text="Open first video", command=lambda: self.open_path_in_explorer(path_one))
        self.watch_b = Button(root, text="Open second video", command=lambda: self.open_path_in_explorer(path_two))
        self.watch_a.place(y=410, x=80)
        self.watch_b.place(y=410, x=480)
        return 0

    def tables(self, path_one, path_two, root):
        self.delete_a = Button(root, text="delete first table",
                               command=lambda: self.destroy_button_label_comparison(1, "delete", path_one))
        self.delete_a.place(y=435, x=10)
        self.delete_b = Button(root, text="delete second table",
                               command=lambda: self.destroy_button_label_comparison(2, "delete", path_two))
        self.delete_b.place(y=435, x=400)

        self.keep_a = Button(root, text="keep first table",
                             command=lambda: self.destroy_button_label_comparison(1, "video"))
        self.keep_a.place(y=435, x=135)
        self.keep_b = Button(root, text="keep second table",
                             command=lambda: self.destroy_button_label_comparison(2, "video"))
        self.keep_b.place(y=435, x=545)

        self.watch_a = Button(root, text="Open first table", command=lambda: self.open_path_in_explorer(path_one))
        self.watch_b = Button(root, text="Open second table", command=lambda: self.open_path_in_explorer(path_two))
        self.watch_a.place(y=410, x=80)
        self.watch_b.place(y=410, x=480)
        return 0

    def unknown_files(self, path_one, path_two, root):
        self.error_label = Label(root, text="ERROR!!! File extension not known.", font=('Helvetica', 20))
        self.error_label.place(x=250, y=200)
        self.delete_a = Button(root, text="delete first table",
                               command=lambda: self.destroy_button_label_comparison(1, "delete", path_one))
        self.delete_a.place(y=435, x=10)
        self.delete_b = Button(root, text="delete second table",
                               command=lambda: self.destroy_button_label_comparison(2, "delete", path_two))
        self.delete_b.place(y=435, x=400)

        self.keep_a = Button(root, text="keep first table",
                             command=lambda: self.destroy_button_label_comparison(1, "video"))
        self.keep_a.place(y=435, x=135)
        self.keep_b = Button(root, text="keep second table",
                             command=lambda: self.destroy_button_label_comparison(2, "video"))
        self.keep_b.place(y=435, x=545)

        self.watch_a = Button(root, text="Open first table", command=lambda: self.open_path_in_explorer(path_one))
        self.watch_b = Button(root, text="Open second table", command=lambda: self.open_path_in_explorer(path_two))
        self.watch_a.place(y=410, x=80)
        self.watch_b.place(y=410, x=480)
        return 0

    def remove_duplicates(self, path_array, root, progress):
        for i in range(len(path_array[1])):
            progress['value'] = (i + 1) / len(path_array[1]) * 100
            for j in range(i + 1, len(path_array[1])):
                if path_array[1][i] == path_array[1][j] and path_array[1][j] != ".DS_Store":
                    new_path = ""
                    path_one = path_array[0][i] + path_array[1][i]
                    for item in path_one:
                        if item == ' ':
                            new_path += ' '
                        else:
                            new_path += item
                    path_one = new_path

                    path_two = path_array[0][j] + path_array[1][j]
                    new_path = ""
                    for item in path_two:
                        if item == ' ':
                            new_path += ' '
                        else:
                            new_path += item
                    path_two = new_path

                    if path_array[1][i].endswith('.jpg') or path_array[1][i].endswith('.png'):
                        control = self.images(path_array, i, j, root)
                        if control == 0:
                            continue

                    elif path_array[1][i].endswith('.doc') or path_array[1][i].endswith('.docx') or \
                            path_array[1][i].endswith('.odt') or path_array[1][i].endswith('.txt') or \
                            path_array[1][i].endswith('.pdf'):
                        control = self.text_files(path_one, path_two, root)
                        if control == 0:
                            continue

                    elif path_array[1][i].endswith('.MP4') or path_array[1][i].endswith('.m4v') or \
                            path_array[1][i].endswith('.mpg'):
                        size_a = os.path.getsize(path_one)
                        size_b = os.path.getsize(path_two)

                        if size_a == size_b:
                            os.remove(path_two)
                        else:
                            control = self.movies(path_one, path_two, root)
                            if control == 0:
                                continue

                    elif path_array[1][i].endswith('.ods') or path_array[1][i].endswith('.xls') or \
                            path_array[1][i].endswith('.xlsm') or path_array[1][i].endswith('.xlsx'):
                        df_a = pd.read_excel(path_one)
                        df_b = pd.read_excel(path_two)
                        if df_a.equals(df_b):
                            os.remove(path_two)
                        else:
                            control = self.tables(path_one, path_two, root)
                            if control == 0:
                                continue
                    else:
                        control = self.unknown_files(path_one, path_two, root)
                        if control == 0:
                            continue

    """ the method checks for same files in path_array_older and removes them. if there are some files in 
    path_array_older which are not in path_array_newer, the method will copy them into the path_array_newer folder"""

    @staticmethod
    def compare_two_folders(path_array_newer, path_array_older):
        for i in range(len(path_array_newer[1])):
            for j in range(len(path_array_older[1])):
                if path_array_newer[1][i] == path_array_older[1][i]:
                    os.remove(path_array_older[0][i] + path_array_older[1][i])

    @staticmethod
    def main(path):
        path_array = [[], []]
        paths = [path]

        while len(paths) != 0:
            path = paths[0]
            paths.pop(0)
            entries = os.scandir(path)
            entry_list = os.listdir(path)
            i = 0

            for entry in entries:
                if entry.is_file():
                    path_array[0].append(path)
                    path_array[1].append(entry_list[i])
                if entry.is_dir():
                    paths.append(path + entry_list[i] + '/')
                i += 1
        return path_array
