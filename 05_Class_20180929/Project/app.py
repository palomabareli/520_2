import modules.bank as bank
import threading

if (__name__ == "__main__"):
    user = input("Nickname: ")    

    try:
        f = threading.Thread(target=bank.select)
        f.start()
    except Exception as ex:
        print('Error in the Thread: {0}'.format(ex.message))

    while (f.isAlive):
        msg = input()
        bank.insert(user, msg)