import json
from functools import partial
from tkinter import Button, Frame, Label, Menu, PhotoImage, Tk, Toplevel, ttk
from tkinter.filedialog import askopenfilename

import cv2
from PIL import Image, ImageTk

from average_filter import average_filter
from contrast_stretching import contrast_stretching
from histogram_equilization import histo_eq
from median_filtering import median_filter

# Global variables
root = Tk()
path = ""
img_label = Label()
la = Label()
img_name = ""
filter_seperator = ttk.Separator(root, orient="horizontal", style="TSeparator")
output_label = Label()

# Load the data from the Data.json file
data = json.load(open("Data.json"))


def print_description(info):
    # Create a new window and show the description
    filewin = Toplevel(root, background="#45438a")
    filewin.title("Description")
    filewin.geometry("600x400")

    # The title and the description of the filters are in the Data.json file
    Title = Label(
        filewin,
        text=info["title"],
        wraplength=500,
        justify="center",
        font="Arial 16 bold",
        width=500,
        background="#45438a",
        foreground="white",
    )
    Title.pack(pady=(0, 20))
    Description = Label(
        filewin,
        text=info["description"],
        wraplength=500,
        font="Arial 12",
        justify="left",
        width=500,
        background="#45438a",
        foreground="white",
    )
    Description.pack(pady=(10, 0))


def get_image_name():
    # Get the global variable img_name and set it to the name of the image
    global img_name

    # Get the path of the image and split it to get the name of the image
    img_name = path.split("/")[-1]


def show_filter(func):
    # Get the global variables and destroy the previous widgets
    global filter_seperator, output_label, img_label
    filter_seperator.destroy()
    output_label.destroy()
    img_label.destroy()

    # Create a new separator
    filter_seperator = ttk.Separator(root, orient="horizontal", style="TSeparator")
    filter_seperator.pack(fill="x", pady=(30, 0))

    # Get the image and the output path from the filter function
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img, output_path = func(img=img, img_name=img_name, img_path=path)

    # Resize the image and show it
    img = Image.open(output_path)
    image = img.resize((280, 280))
    output_label = Label(
        root, text="Output image", font="Arial 12 bold", foreground="#45438a"
    )
    output_label.pack(pady=(10, 0))
    my_img = ImageTk.PhotoImage(image)
    img_label = Label(
        root, image=my_img, width=280, height=280, borderwidth=1, relief="solid"
    )
    img_label.image = my_img
    img_label.pack(pady=(20, 0))


def load_filters():
    # make label and frame for filters and buttons for filters
    label = Label(
        root,
        text="Choose any filter to start",
        font="Arial 12 bold",
        foreground="#45438a",
    )
    label.pack(pady=5)

    # make a frame for the buttons
    frame = Frame(root)

    # make a list of filters and their functions
    filters = [
        "Average Filter",
        "Contrast Stertching",
        "Histogram Equalization",
        "Median Filter",
    ]
    functions = [average_filter, contrast_stretching, histo_eq, median_filter]

    # make a button for each filter
    for x in range(len(filters)):
        btn = Button(
            frame,
            text=filters[x],
            command=partial(show_filter, functions[x]),
            font="Arial 12 bold",
            borderwidth=0,
            width=20,
            height=2,
            background="#45438a",
            fg="white",
        )
        btn.grid(row=0, column=x, padx=2)

    # pack the frame
    frame.pack()


def clear_screen():
    # Clear the screen before showing the image
    for child in root.winfo_children():
        if not isinstance(child, Menu):
            child.destroy()


def pick_image():
    # Clear the screen before showing the image
    clear_screen()

    # Get the global path variable and set it
    global path

    # Ask the user to choose an image
    path = askopenfilename()

    # Check if the user chose an image
    if len(path) > 0:
        try:
            # open the image and resize it and change it to a tkinter image
            image = Image.open(path)
            image = image.resize((280, 280))
            my_img = ImageTk.PhotoImage(image)

            # get the global label variable and set it
            global la

            # destroy the previous label and create a new one
            la.destroy()

            # create a label and pack it
            label = Label(
                root, text="Chosen image", font="Arial 12 bold", foreground="#45438a"
            )
            label.pack(pady=(5, 0))

            # create a label and pack it
            la = Label(
                root, image=my_img, width=280, height=280, borderwidth=1, relief="solid"
            )
            la.image = my_img
            la.pack(pady=(5, 10))

            # create a separator and pack it
            separator = ttk.Separator(root, orient="horizontal")
            separator.pack(fill="x", pady=20)

            # get the image name
            get_image_name()

            # load the filters
            load_filters()

        except Exception:
            # if the user chose an invalid image, show an error message
            la = Label(
                root,
                text="Please choose a valid image!",
                font="Arial 12 bold",
                fg="red",
            )
            la.pack(pady=10)
    else:
        # Set the background color of the window
        bg = PhotoImage(file="Images/Welcome.png")
        label = Label(root, image=bg)
        label.image = bg
        label.place(x=0, y=0, height=850, width=1080)
        label.pack()


def create_menu():
    # create menu bar and add menu items
    menubar = Menu(
        root, tearoff=0, background="#45438a", foreground="white", font="Arial 12 bold"
    )

    # create file menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=pick_image)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create About menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(
        label="Description", command=partial(print_description, data["description"])
    )
    for filter in data["filters"]:
        helpmenu.add_command(
            label=filter["title"], command=partial(print_description, filter)
        )
    menubar.add_cascade(label="About", menu=helpmenu)

    # display the menu bar on the window
    root.config(menu=menubar)

    # create separator
    global filter_seperator
    filter_seperator = ttk.Separator(root, orient="horizontal", style="TSeparator")


def main():
    # get global root variable
    global root

    # Create the main window of the application
    root.title("Image Processing Project")

    # Set the size of the window
    root.geometry("1080x850")

    # Set the background color of the window
    bg = PhotoImage(file="Images/Welcome.png")
    label = Label(root, image=bg)
    label.image = bg
    label.place(x=0, y=0, height=850, width=1080)
    label.pack()

    # Create the menu
    create_menu()

    # Start rendering the application
    root.mainloop()


# Run the main function
if __name__ == "__main__":
    main()
