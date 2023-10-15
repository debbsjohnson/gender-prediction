from tkinter import *

# the request will be used for making request to the api
import requests

# tkinter message box to display errors
from tkinter.messagebox import showerror

def predict_gender():
    # executes when code has no erros
    try:
        # getting the input from entry
        entered_name = name_entry.get()
        # making request to the api, the user's entered name is injected in the url
        response = requests.get(f"https://api.genderize.io/?name={entered_name}").json()
        # getting name from the response
        name = response["name"]
        # getting gender from response
        gender = response["gender"]
        # getting probability from response
        probability = 100 * response["probability"]
        # adding name to the label that was empty, using uppercase
        name_label.config(text="the name is " + name.upper())
        # adding gender to the label that was empty, using uppercase
        gender_label.config(text="the name is " + gender.upper())
        # adding probability to the label that was empty
        probability_label.config(text="I'm " + str(probability) + "% " + "accurate")
    
    except:
        showerror(title="error", message="an error occured! make sure you have the right internet connection or you have entered the correct data")

# select colours for the application
pink = "#fff8f9"
ruby = "#E0115F"

# creating the main window
window = Tk()

window.configure(bg=ruby)

#defining the dimensions of the window, width(325), height(300), 500 + 200 center the window
window.geometry("325x300+500+200")
# title of the application
window.title("Gender Prediction")
# this makes the window unresizable 
window.resizable(height=FALSE, width=FALSE)

"""the two frames"""
# this is the top frame from inside the main window
top_frame = Frame(window, bg=ruby, width=325, height=80)
top_frame.grid(row=0, column=0)

# bottom frame from inside the main window
bottom_frame = Frame(window, width=300, height=80)
bottom_frame.grid(row=1, column=0)

top_frame.configure(bg=ruby)
bottom_frame.configure(bg=ruby)

# this label is for the big title that's inside the top_frame
first_label = Label(top_frame, text="GENDER PREDICTION", bg=ruby, fg=pink, pady=10, padx=20, justify=CENTER, font=("Poppins 20 bold"))
first_label.grid(row=0, column=0)

second_label = Label(bottom_frame, text="Provide a name and I will predict its gender :|", bg=ruby, fg=pink, pady=10, padx=20, justify=CENTER, font=("Poppins 10"))
second_label.grid(row=1, column=0)


# create a frame for the input section
input_frame = Frame(bottom_frame, width=300, height=150, bg=ruby)
input_frame.grid(row=1, column=0)

label = Label(input_frame, text="NAME:", font=("Poppins 10 bold"), bg=ruby, justify=LEFT)
label.grid(row=0, column=0, padx=10, pady=10)

name_entry = Entry(input_frame, width=25, font=("Poppins 15 bold"))
name_entry.grid(row=0, column=1, padx=10, pady=10)

predict_button = Button(input_frame, text="PREDICT", bg=pink, fg=ruby, font=("Poppins 10 bold"), command=predict_gender)
predict_button.grid(row=1, column=0, columnspan=2, padx=14, pady=14)

# create a frame for the results
result_frame = Frame(bottom_frame, width=300, height=100, bg=ruby)
result_frame.grid(row=2, column=0)

name_label = Label(result_frame, text="", font=("Poppins 10 bold"), bg=pink, fg=ruby)
name_label.pack(pady=5)

gender_label = Label(result_frame, text="", font=("Poppins 10 bold"), bg=pink, fg=ruby)
gender_label.pack(pady=5)

probability_label = Label(result_frame, text="", font=("Poppins 10 bold"), bg=pink, fg=ruby)
probability_label.pack(pady=5)



window.mainloop()




