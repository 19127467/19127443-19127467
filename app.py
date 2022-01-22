import os
import webbrowser
filename = 'file://'+os.getcwd()+'/' + 'templates/index.html'
webbrowser.open_new(filename)
webbrowser.open(filename)