

# read the file

# open the file
import tkinter as tk
import matplotlib.pyplot as plt
file_ = open("text.txt", "r")


# create a list from the lines

# read the lines
lines = file_.readlines()
print(lines)


# plot each letter in a case like mots croisés

# create a list of lists
list_of_lists = []

# loop through the lines
for line in lines:
    # create a list of letters
    list_of_letters = []
    # loop through the letters
    for letter in line:
        # append the letter to the list
        list_of_letters.append(letter)
    # append the list of letters to the list of lists
    list_of_lists.append(list_of_letters)


# show the letters in tkinter grid,

# create a window
window = tk.Tk()

# create a grid
for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        # create a label
        label = tk.Label(
            text=list_of_lists[i][j],
            width=2,
            height=1,
            borderwidth=1,
            relief="solid"
        )
        # put the label in the grid
        label.grid(row=i, column=j)

# show the window
window.mainloop()
