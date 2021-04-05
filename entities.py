import time
class Timer:
    def __init__(self, cooldown):
        self.last_invoke = time.process_time()
        self.cooldown = cooldown
    def relax(self):
        cur_time = time.process_time()
        if cur_time - self.last_invoke > self.cooldown:
            self.last_invoke = cur_time
            return True
        else:
            return False

import winsound
class Sound:
    def __init__(self, path):
        self.path = path
    def play(self):
        winsound.PlaySound(self.path, winsound.SND_FILENAME)

import webbrowser
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
browser = webbrowser.get('Chrome')

class Image:
    def __init__(self, path):
        self.path = path
    def show(self):
        browser.open(self.path)
