from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.ttk import Progressbar

import synchronizer


class SyncGui:
    """TODO make multithreading or multiprocessing for calculating"""
    path = '/Users/andreas/Desktop/test_ordner/'
    paths = [[], []]

    def change_path(self):
        self.path = askdirectory()
        self.path += '/'

    def start_work(self):
        if self.path != '':
            self.progress_label = Label(self.root, text="progress: ")
            self.progress_label.place(x=10, y=466)
            self.progress.place(x=90, y=469)
            self.paths = synchronizer.Synchronize.main(self.path)
            synchronizer.Synchronize.remove_duplicates(self.paths, self.root, self.progress)
        else:
            messagebox.showerror("path ERROR", "path can't be empty!!! Choose another path.")

    def start_thread(self):
        self.start_work()
        messagebox.showinfo("finished work", "The chosen folder has been synchronized")
        self.progress_label.destroy()
        self.progress.destroy()

    def __init__(self):
        self.root = Tk()
        self.root.title("synchronize your folders")
        self.root.minsize(810, 500)
        self.root.maxsize(810, 500)
        self.root.configure(bg='grey')

        self.choose_path = Button(self.root, text="open directory", command=self.change_path).place(y=463, x=684)
        self.commit_work = Button(self.root, text="start work", command=self.start_thread).place(y=463, x=594)
        self.progress = Progressbar(self.root, orient=HORIZONTAL, length=480, mode='determinate')

        self.root.mainloop()


if __name__ == '__main__':
    SyncGui()
