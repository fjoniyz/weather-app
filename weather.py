import requests
import tkinter as tk
from tkinter import *
class App(tk.Tk):
    dimension = "500x500"
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Weather App")
        self.geometry(self.dimension)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="GET", command=self.get_info)
        self.button_quit = tk.Button(self, text="QUIT", command=quit)
        self.button_quit.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.entry.place(relx=0.5, rely=0.5, anchor=CENTER)

    def get_info(self):
        api_key = 'ENTER API KEY HERE' #here you should enter your own api key in order for the app to work
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.entry.get()}&units=metric&appid={api_key}'
        code = requests.get(url).status_code
        if code == 404:
            not_found = tk.Label(text="Could not find the city you were looking for :(")
            not_found.place(relx=0.5, rely=0.4, anchor=CENTER)
            return 
        if code == 500:
            error_server = tk.Label(text="Oops, it seems like the third party app is down. Come back in a bit")
            error_server.place(relx=0.5, rely=0.4, anchor=CENTER)
            return
        r = requests.get(url).json()
        tk.Tk.__init__(self)
        self.title(self.entry.get().upper())
        self.geometry(self.dimension)
        self.button = tk.Button(self, text="QUIT", command=quit)
        self.button.place(relx=0.5, rely=0.6, anchor=CENTER)
        max_temp_label = tk.Label(text="Max temp is: ")
        max_temp_res = tk.Label(text=self.max_temp(r))
        min_temp_label = tk.Label(text="Min temp is: ")
        min_temp_res = tk.Label(text=self.min_temp(r))
        humidity_label = tk.Label(text="Humidity")
        humidity_res = tk.Label(text=self.humidity(r))
        actual_temp_label = tk.Label(text="Actual temp: ")
        actual_temp_res = tk.Label(text=self.temp_now(r))
        #packing
        actual_temp_label.pack()
        actual_temp_res.pack()
        humidity_label.pack()
        humidity_res.pack()
        min_temp_label.pack()
        min_temp_res.pack()
        max_temp_label.pack()
        max_temp_res.pack()

    def max_temp(self, r):
        return r['main']['temp_max']

    def min_temp(self, r):
        return r['main']['temp_min']

    def humidity(self, r):
        return r['main']['humidity']

    def temp_now(self, r):
        return r['main']['temp']

    def quit(self, root):
        root.destroy()
top = App()
top.mainloop()