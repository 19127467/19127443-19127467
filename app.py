import os
import webbrowser
filename = 'file://'+os.getcwd()+'/' + 'index.html'
webbrowser.open_new(filename)
webbrowser.open(filename)