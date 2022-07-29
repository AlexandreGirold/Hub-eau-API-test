from datetime import datetime
import os



def contrendu():
    date = datetime.today().strftime('%Y-%m-%d')
    name = "log_test_" + date + ".txt"
    if os.path.exists(name) :
        os.remove(name)

def write_contrendu(text):
    date = datetime.today().strftime('%Y-%m-%d')
    name = "log_test_" + date + ".txt"
    with open(name, 'a') as file:
        file.write(text + "\n")
    file.close()

