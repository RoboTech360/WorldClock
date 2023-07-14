import datetime
import pytz
import tkinter as tk

class WorldClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("World Clocks (github.com/RoboTech360)")

        # Define the time zones and their corresponding city names
        self.time_zones = {
            'America/New_York': 'America/New York',
            'Europe/Oslo': 'Norway/Oslo',
            'Asia/Kolkata': 'India/New Delhi',
            'Asia/Shanghai': 'China/Shanghai',
            'Asia/Tokyo': 'Japan/Tokyo'
        }

        self.clock_labels = {}

        self.create_clock_labels()

        # Set the background color of the application window
        self.master.configure(bg='black')

    def create_clock_labels(self):
        # Define the font style for the labels

        #frame = tk.Frame(self.master, bg='red')  # Create a frame with the desired background color
        #frame.pack(fill='both', expand=True)
        
        #canvas = tk.Canvas(self.master, bg='black')  # Create a canvas with the desired background color
        #canvas.pack(fill='both', expand=True)
        
        font_style = ('Consolas', 12, 'normal')

        for tz, city in self.time_zones.items():
            # Create a label for each clock
            #below line commented after commenting canvas definition
            #clock_label = tk.Label(self.master, font=font_style, anchor='w')
            clock_label = tk.Label(self.master, font=font_style, anchor='w', bg="black")
            clock_label.pack(fill='x')
            self.clock_labels[tz] = clock_label

    def update_clocks(self):
        for tz, clock_label in self.clock_labels.items():
            current_time = datetime.datetime.now(pytz.timezone(tz))
            date_str = current_time.strftime('%Y-%m-%d')
            time_str = current_time.strftime('%H:%M:%S')
            color = self.get_font_color(tz)
            formatted_time = f'{self.time_zones[tz]:<20} {date_str}    {time_str}'  # Indent the time
            clock_label.configure(text=formatted_time, fg=color)

        self.master.after(1000, self.update_clocks)  # Update every second

    def get_font_color(self, tz):
        # Define the font colors for each time zone
        font_colors = {
            'America/New_York': 'lightgreen',
            'Europe/Oslo': 'white',
            'Asia/Kolkata': 'orange',
            'Asia/Shanghai': 'magenta',
            'Asia/Tokyo': 'red'
        }
        return font_colors.get(tz, 'black')  # Default font color is black

if __name__ == '__main__':
    # Create the Tkinter root window
    root = tk.Tk()

    # Create an instance of the WorldClockApp
    app = WorldClockApp(root)

    # Start updating the clocks
    app.update_clocks()

    # Start the Tkinter event loop
    root.mainloop()
