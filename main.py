from tkinter import Toplevel, Button, Label, Frame, Menu, Tk, PhotoImage
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import ttk
from functools import partial
from average_filter import average_filter
from contrast_stretching import contrast_stretching
from histogram_equilization import histo_eq
from median_filtering import median_filter
import cv2
import json


# Global variables
root = Tk()
path = ""
img_label = Label()
la = Label()
img_name = ""
data = json.load(open("Data.json"))
filter_seperator = ttk.Separator(root, orient="horizontal", style="TSeparator")
output_label = Label()


def print_description(info):
    filewin = Toplevel(root, background='#45438a')
    filewin.title("Description")
    filewin.geometry("600x400")
    Title = Label(filewin, text=info["title"], wraplength=500, justify="center", font="Arial 16 bold", width=500, background='#45438a', foreground="white")
    Title.pack(pady=(0, 20))
    Description = Label(filewin, text=info["description"], wraplength=500, font="Arial 12", justify="left", width=500, background='#45438a', foreground="white")
    Description.pack(pady=(10, 0))


def get_image_name():
    global img_name
    img_name = path.split("/")[-1]


def show_filter(func):
    global filter_seperator, output_label
    filter_seperator.destroy()
    output_label.destroy()
    filter_seperator = ttk.Separator(root, orient="horizontal", style="TSeparator")
    filter_seperator.pack(fill="x", pady=(30, 0))
    global img_label
    img_label.destroy()
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img, output_path = func(img=img, img_name=img_name)
    img = Image.open(output_path)
    image = img.resize((280, 280))
    output_label = Label(root, text="Output image", font='Arial 12 bold', foreground='#45438a')
    output_label.pack(pady=(10, 0))
    my_img = ImageTk.PhotoImage(image)
    img_label = Label(
        root, image=my_img, width=280, height=280, borderwidth=1, relief="solid")
    img_label.image = my_img
    img_label.pack(pady=(20, 0))


def load_filters():
    label = Label(root, text="Choose any filter to start", font='Arial 12 bold', foreground='#45438a')
    label.pack(pady=5)
    frame = Frame(root)
    filters = [
        "Average Filter",
        "Contrast Stertching",
        "Histogram Equalization",
        "Median Filter",
    ]
    functions = [average_filter, contrast_stretching, histo_eq, median_filter]
    for x in range(len(filters)):
        btn = Button(frame, text=filters[x], command=partial(show_filter, functions[x]), font='Arial 12 bold', borderwidth=0, width=20, height=2, background='#45438a', fg='white')
        btn.grid(row=0, column=x, padx=2)
    frame.pack()


def clear_screen():
    for child in root.winfo_children():
        if not isinstance(child, Menu):
            child.destroy()


def pick_image():
    clear_screen()
    global path
    path = askopenfilename()
    if len(path) > 0:
        try:
            image = Image.open(path)
            image = image.resize((280, 280))
            my_img = ImageTk.PhotoImage(image)
            global la
            la.destroy()
            label = Label(root, text="Chosen image", font='Arial 12 bold', foreground='#45438a')
            label.pack(pady=(5, 0))
            la = Label(
                root, image=my_img, width=280, height=280, borderwidth=1, relief="solid")
            la.image = my_img
            la.pack(pady=(5, 10))
            separator = ttk.Separator(root, orient="horizontal")
            separator.pack(fill="x", pady=20)
            get_image_name()
            load_filters()
        except Exception as e:
            print(e)
            la = Label(root, text="Please choose a valid image!", font='Arial 12 bold', fg='red')
            la.pack(pady=10)
    else:
        la = Label(root, text="Click File and choose open to open an image", font='Arial 12 bold', fg='45438a')
        la.pack(pady=10)


def create_menu():
    menubar = Menu(root, tearoff=0, background='#45438a', foreground='white', font='Arial 12 bold')
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=pick_image)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Description", command=partial(print_description, data["description"]))
    for filter in data["filters"]:
        helpmenu.add_command(label=filter["title"], command=partial(print_description, filter))
    menubar.add_cascade(label="About", menu=helpmenu)

    root.config(menu=menubar)

    global filter_seperator
    filter_seperator = ttk.Separator(root, orient="horizontal", style="TSeparator")


def main():
    global root
    root.title("Image Processing Project")
    root.geometry("1080x850")
    bg = PhotoImage(file="Images/Welcome.png")
    label = Label(root, image=bg)
    label.image = bg
    label.place(x=0, y=0, height=850, width=1080)
    label.pack()
    ###############
    #             #
    # Design here #
    #             #
    ###############
    create_menu()

    # Start rendering the application
    root.mainloop()


if __name__ == "__main__":
    main()
