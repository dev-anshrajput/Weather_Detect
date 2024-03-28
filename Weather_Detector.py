import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    location = location_entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a location.")
        return

    api_key = "ee83a570ea9af60b783022da6dff5224"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_conditions = data['weather'][0]['description']
            weather_info = f"Weather in {location}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWeather Conditions: {weather_conditions.capitalize()}"
            weather_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", f"Failed to fetch weather data. Error code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch weather data. Please check your internet connection.")

root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill='both')

# Left side (Enter Location)
location_label = tk.Label(frame, text="Enter Location:")
location_label.grid(row=0, column=0, sticky="w")

location_entry = tk.Entry(frame)
location_entry.grid(row=1, column=0, sticky="ew", pady=5)

get_weather_button = tk.Button(frame, text="Get Weather", command=get_weather)
get_weather_button.grid(row=2, column=0, sticky="ew", pady=5)

# Right side (Weather Results)
weather_label = tk.Label(frame, text="", font=('Helvetica', 12))
weather_label.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=10)

# Configure grid weights to make the right column expandable
frame.grid_columnconfigure(1, weight=1)

root.mainloop()
