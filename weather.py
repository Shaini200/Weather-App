#To create a weather app in Python using Tkinter and the OpenWeatherMap API

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather app")
root.geometry("800x700+300+50")
root.resizable(False,False)

def getWeather():
    city = textfield.get()
    
    try:
        # Use a valid user_agent
        geolocator = Nominatim(user_agent="WeatherApp")
        location = geolocator.geocode(city)
        if location is None:
            messagebox.showerror("Error", "City not found!")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        #print(result)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fba4bd38aece509bdecf64750ddb96a3"
        print(api)
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        # Add additional functionality to display the timezone or handle the location details

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")



#search box
search_img=PhotoImage(file="search.png")
myimage=Label(image=search_img)
myimage.place(x=20,y=30)

textfield=tk.Entry(root,justify="left",width=15,font=("Albertus Medium",20,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=70,y=50)
textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=43)


#logo
logo_img=PhotoImage(file="logo1.png")
myimage_logo=Label(image=logo_img)
myimage_logo.place(x=120,y=120)

#bottom box
frame_img=PhotoImage(file="box.png")
myimage_frame=Label(image=frame_img)
myimage_frame.pack(padx=10,pady=10,side=BOTTOM)

#name
name=Label(root,font=("Arial",15,"bold"))
name.place(x=30,y=120)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=150)


#label
label1=Label(root,text="WIND",font=("Arial",14,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=70,y=600)

label2=Label(root,text="HUMIDITY",font=("Arial",14,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=230,y=600)

label3=Label(root,text="DESCRIPTION",font=("Arial",14,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=410,y=600)

label4=Label(root,text="PRESSURE",font=("Arial",14,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=620,y=600)

#tempture
t=Label(font=("Arial",50,"bold"),fg="#ee666d")
t.place(x=120,y=300)
#condition
c=Label(font=("Arial",14,"bold"))
c.place(x=120,y=370)

w=Label(text=".....",font=("Arial",17,"bold"),bg="#1ab5ef")
w.place(x=70,y=630)
h=Label(text=".....",font=("Arial",17,"bold"),bg="#1ab5ef")
h.place(x=240,y=630)
d=Label(text=".....",font=("Arial",17,"bold"),bg="#1ab5ef")
d.place(x=410,y=630)
p=Label(text=".....",font=("Arial",17,"bold"),bg="#1ab5ef")
p.place(x=630,y=630)

root.mainloop()
