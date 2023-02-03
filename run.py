import threading

import os

def fuck(file):

    os.system(f"python {file}")

    

    

    

threading.Thread(target=fuck, args=("moon.py")).start();

threading.Thread(target=fuck, args=("devamke.py")).start();
