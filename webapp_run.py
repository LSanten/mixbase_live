"""
Leon Santen

This code runs the web application and accesses MixBase.py / run.py. MixBase.py is for development purposes. run.py is for usage purposesself.

To STOP server: hit ctrl+c terminal.

This webapp was developed with the great tutorials by Corey Schafer - https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
"""
from webapp import app #imports from __init__.py

if __name__ == '__main__':
    app.run(debug=False)
