import time
from pages.demoqa import DemoQa
from pages.alerts import Alerts



def viewport(self, name, content):
    self.name = 'head > meta viewport'
    self.content = 'width=device-width,initial-scale=1'

