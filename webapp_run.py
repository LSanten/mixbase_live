"""
Leon Santen

This code runs the web application and accesses MixBase.py / run.py. MixBase.py is for development purposes. run.py is for usage purposesself.

Please set the debug_mode to 0 for "off" and 1 for "on".
To STOP server: hit ctrl+c terminal.

This webapp was developed with the great tutorials by Corey Schafer - https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
"""
from webapp import app #imports from __init__.py

if __name__ == '__main__':
    app.run(debug=True)
    webbrowser.open_new("http://127.0.0.1:5000/")
