# Project Name: Noise Sense


# Team Details :
# 1. Mithuna K (mithunakamalanathan@gmail.com)
# 2. Nethara G (netharagengesh@gmail.com)
# 3. Sandhiya S (sandhiyashanmugam2007@gmail.com)
# 4. Sanjai M S (sanjaims103@gmail.com)
# 5. Srisanth S (ssrisanth06@gmail.com)


# import necessary modules
import os
import time
import sounddevice as sd
import numpy as np
import datahandel as dh
import pywhatkit as pwk

def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def admin():
    # Prompt for admin credentials
    useid = input("Enter staff user id : ")
    pas = input("Enter your password : ")
    try:
        # Verify admin credentials using datahandel module
        result = dh.check_admin(useid, pas)
        if result == "verified":
            print("The admin logged in successfully...")
            time.sleep(1)
            return "y"  # Return 'y' to indicate successful login
        else:
            print("Invalid username or password")
            return "n"  # Return 'n' for failed login
    except Exception as e:
        print(f"Authentication error: {e}")
        return "n"  # Return 'n' for any authentication errors

def student():
    # Prompt for student credentials
    useid = input("Enter student user id : ")
    pas = input("Enter your password : ")
    try:
        # Verify student credentials using datahandel module
        result = dh.check_student(useid, pas)
        if result == "verified":
            print("The student logged in successfully...")
            time.sleep(1)
            return "y"  # Return 'y' to indicate successful login
        else:
            print("Invalid username or password")
            return "n"  # Return 'n' for failed login
    except Exception as e:
        print(f"Authentication error: {e}")
        return "n"  # Return 'n' for any authentication errors

def record_audio(device, duration=3, samplerate=44100):
    # Record audio from the specified device for the given duration
    try:
        print(device)
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, device=device)
        sd.wait()  # Wait until recording is complete
        return audio  # Return the recorded audio data
    except sd.PortAudioError as e:
        print(f"Audio recording error: {e}")
        return None  # Return None if recording fails

def calculate_rms(audio):
    # Calculate the Root Mean Square (RMS) value of the audio data
    if audio is None:
        return 0.0  # Return 0.0 if audio is None
    return np.sqrt(np.mean(np.square(audio)))  # Compute RMS value

def sound(devices, duration=3):
    # Measure noise levels for a list of audio devices
    rms_values = []  # Store RMS values for each device
    # Filter valid devices with input channels
    valid_devices = [i for i, d in enumerate(sd.query_devices()) if d['max_input_channels'] > 0]
    for device in devices:
        if device not in valid_devices:
            print(f"Invalid device index: {device}")
            continue
        # Record audio and calculate RMS for the device
        audio = record_audio(device, duration)
        rms = calculate_rms(audio)
        rms_values.append((device, rms))  # Store device index and RMS value
    return rms_values  # Return list of (device, RMS) tuples

def main():
    # Display project title and user type menu
    print("This is the project created by Fist year students of CSE and AIML".center(150, "*"))
    print("1.Staff\n2.Student\n3.Exit")
    try:
        choice = int(input("Enter the user type : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(1)
        return  # Exit if input is invalid

    clear_screen()  # Clear the screen for the next menu
    match choice:
        case 1:  # Admin mode
            ch = admin()  # Authenticate admin
            while ch.lower() == "y":  # Continue if login is successful
                clear_screen()
                print("1.Single Area Check\n2.Continuous Area Checking\n3.Exit")
                try:
                    choice = int(input("Enter your choice : "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(1)
                    ch = "n"  # Exit loop on invalid input
                    continue

                match choice:
                    case 1:  # Single Area Check
                        clear_screen()
                        print(sd.query_devices())  # Display available audio devices
                        try:
                            device = int(input("Enter the device to be checked : "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            time.sleep(1)
                            continue
                        clear_screen()
                        rms = sound([device])  # Measure noise for single device
                        if rms:
                            print(f"Device {rms[0][0]} RMS Level: {rms[0][1]:.4f}")
                            if rms[0][1] <= 0.0521:
                                print("Low...")  # Classify as low noise
                            else:
                                print("High...")  # Classify as high noise
                        time.sleep(2)
                    case 2:  # Continuous Area Checking
                        clear_screen()
                        print("Continuous Area checking Mode....".center(150, "*"))
                        while True:  # Run indefinitely until interrupted
                            device = [0, 1, 2]  # Default devices to monitor
                            rms = sound(device)  # Measure noise for all devices
                            for value in rms:
                                if value[1] <= 0.0521:
                                    level = "Low..."  # Classify as low noise
                                else:
                                    level = "High..."  # Classify as high noise
                                    current_time = time.localtime()
                                    hours = current_time.tm_hour
                                    minutes = current_time.tm_min + 1
                                    # Send WhatsApp notification for high noise
                                    pwk.sendwhatmsg(
                                        "+919342672711",
                                        f"The Noise is high at {value[0]}",
                                        hours,
                                        minutes
                                    )
                                print(f"Device {value[0]} RMS Level: {value[1]:.4f}         {level}")
                    case 3:  # Exit admin mode
                        clear_screen()
                        print("The program has been exited")
                        time.sleep(1)
                        ch = "n"  # Exit admin loop
                    case _:  # Invalid choice
                        clear_screen()
                        print("Invalid input...")
                        time.sleep(1)
                        ch = "n"  # Exit admin loop
        case 2:  # Student mode
            clear_screen()
            ch1 = student()  # Authenticate student
            print("Checking for the Quietest Hall")
            if ch1.lower() == "y":  # Proceed if login is successful
                device = [0, 1, 2]  # Default devices to check
                rms = sound(device)  # Measure noise for all devices
                if rms:
                    # Find the device with the lowest RMS value
                    quieter_device = min(rms, key=lambda x: x[1])
                    print(f"\nQuietest place is from Device {quieter_device[0]} with RMS {quieter_device[1]:.4f}")
                time.sleep(5)  # Pause to display result
        case 3:  # Exit program
            clear_screen()
            print("The program has been exited....")
            time.sleep(1)
        case _:  # Invalid user type
            clear_screen()
            print("Invalid Input..")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()  # Run the main program
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")  # Handle Ctrl+C
    except Exception as e:
        print(f"Program error: {e}")  # Handle other exceptions