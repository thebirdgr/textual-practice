# python script to read from status.json and use textual to display
# and update the status of the file. 
import json
import os
from textual.app import App
from textual import events

class mainApp(App):
    COLORS = {
        True: "maroon",
        False: "olive"
    }
    status = {}
    
    def on_mount(self) -> None:
        self.screen.styles.background = "fuchsia"
    
    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            if int(event.key) < len(self.COLORS):
                self.screen.styles.background = self.COLORS[int(event.key)]

    def poll(self):
        with open('status.json') as f:
            data = json.load(f)
        self.status = data['status']


if __name__ == '__main__':
    app = mainApp()
    app.run()
    while True:
        app.poll()
        