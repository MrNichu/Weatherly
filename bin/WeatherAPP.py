#Importing required modules----------------------------------------------
import json
import requests
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
#Defining my find_weather function here-----------------------------------
def find_weather(e):
    city_name = e.get()
    if city_name == 'Enter city name !':
        messagebox.showerror("hello there !","Please enter a valid city name.")
        root.quit()
    e.delete(0,END)
    #connecting to API-------------------
    api_key = "d3d82d78f63d0f00e085ab7042d34cdd" #my unique API key---------
    try:
        url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
        #whatever content of data the API returns(in JSON format),we load it and store in a variable called response-----
        api_response = json.loads(url.content)
    except Exception as e:
        api_response="Error connecting to API "
    #Filtering the required data from the returned data and shoving it on screen-------------------
    location = api_response['name']
    current_temp = round((api_response['main']['temp']-273.15),1)
    feels = round((api_response['main']['feels_like']-273.15),1)

    #creating labels of the filtered data to display them on my canvas window--------------
    location_label = Label(root,text="Location : "+str(location),font=("Helvetica", 15))
    feels_label = Label(root,text="Feels like : "+str(feels)+" 'C",font=("Helvetica", 15))
    current_temp_label = Label(root, text="Current Temparature : " + str(current_temp)+ " 'C",font=("Helvetica", 15),)

    #creating windows and shoving all of these on my screen-----------------------------------
    global location_window
    global min_temp_window
    global current_temp_window
    # displaying text ressults on screen
    location_window = my_canvas.create_window(100, 200,anchor="nw",window=location_label)
    min_temp_window = my_canvas.create_window(100, 225,anchor="nw",window=feels_label)
    current_temp_window = my_canvas.create_window(100, 250, anchor="nw",window=current_temp_label)


#creating and naming root window----------------------------------------------

root = Tk()
root.geometry("500x750")
root.title("Weatherly")
root.iconbitmap('weatherly.ico')
root.resizable(False,False)
#creating canvas that goes on top of root window--------------------------

my_canvas = Canvas(root, width=500, height=750)
my_canvas.pack(fill="both", expand=True)
#Creating background image and shoving it on canvas--------------------

my_img = ImageTk.PhotoImage(Image.open('weather.jpg'))
my_canvas.create_image(0,0,image=my_img, anchor="nw")
#creating Entry box,and search button-------------------------------------------------------------

e = Entry(root, font=("Helvetica 44 italic",10),width=35,borderwidth=3)
e.insert(-1,'Enter city name !')
#Rounded button (search)----------------------------------------------------------------------

#button_img = ImageTk.PhotoImage(Image.open('Search (1).png'))
search_button = Button(root, text='Search !',font=("Helvetica",10),command=lambda: find_weather(e),borderwidth=1)



#Displaying everything on the canvas window that we created-----------------------------------------

my_canvas.create_text(260,70,text="Welcome to weatherly.",font=("Helvetica",25),fill = "white")
entry_window = my_canvas.create_window(128,110,anchor="nw",window=e)
search_button_window = my_canvas.create_window(225,150,anchor="nw",window=search_button)
my_canvas.create_text(450,680,text="~ By Arijit",font=("Helvetica",7),fill = "white")

#looping root
root.mainloop()