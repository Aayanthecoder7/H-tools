from tkinter import *
import webbrowser, os, pyautogui, time, random,subprocess, pyperclip

root = Tk()
root.title("Hacker tool")
root.geometry("500x500")
root.config(background="black")

# open website
def open_website():
    website = entry.get()
    webbrowser.open(website)
label = Label(root, text="Enter website URL:(start with www.website.com)", fg="white", bg="black")
label.pack()

entry = Entry(root, width=50)
entry.pack()

button = Button(root, text="Open Website", command=open_website)
button.pack()

#shutdown pc
def shutdown_pc():
    os.system("shutdown /s /t 1")
label1 = Label(root, text="This shutsdown your PC:", background="black", foreground="white")
label1.place(x=180, y=390)
button1 = Button(root, text="SHUTDOWN PC", command=shutdown_pc, background="Red")
button1.place(x=200, y=410)

#Crazy mouse
def move_mouse():
    while True:
        screen_width, screen_height = pyautogui.size()
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)
        pyautogui.moveTo(random_x, random_y)
        time.sleep(1)

labelmouse = Label(root, text="(press window to exist)This button makes your mouse move crazy:", foreground="white", background="black")
labelmouse.pack()

buttonmouse = Button(root, text="AFK MOUSE", command=move_mouse)
buttonmouse.pack()      

#Network finder
def get_key():
    wifi_name = entry.get()
    command = ['netsh', 'wlan', 'show', 'profile', 'name=' + wifi_name, 'key=clear']
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        if "Key Content" in line:
            key_content = line.split(":")[1].strip()
            key_label.config(text=f"{key_content}")
            break
    else:
        key_label.config(text="WiFi Key not found")

def copy_code():
    key_text = key_label.cget("text")
    if key_text:
        pyperclip.copy(key_text)


label = Label(root, text="(This tool gets your wifi password) Enter WiFi Name:", background="black", foreground="white")
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text="Show WiFi Key", command=get_key, background="grey")
button.pack()
Info = Label(root, text="Your Network key:")
Info.pack()
key_label = Label(root, text="🗿🗿🗿", wraplength=250)
key_label.pack()
small_copy = Button(root, background="cyan", text="Copy🔎", command=copy_code)
small_copy.pack()
#Ip finder
def find_ip():
    try:
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        if result.returncode == 0:
            ip_output = result.stdout
            for line in ip_output.split('\n'):
                if 'IPv4 Address' in line:
                    ip_address = line.split(':')[-1].strip()
                    ip_label.config(text=f"{ip_address}")
                    return
            ip_label.config(text="IPv4 Address not found")
        else:
            ip_label.config(text="Failed to run ipconfig")
    except Exception as e:
        ip_label.config(text=f"Error: {e}")

def copy_code1():
    key_text = ip_label.cget("text")
    if key_text:
        pyperclip.copy(key_text)

labelipp = Label(root, text="This button give the Ip address of the Computer:", background="Black", foreground="white")
labelipp.pack()
ip_label = Label(root, text="🗿🗿🗿", font=("Arial", 12))
ip_label.pack()
button_ip = Button(root, text="Get IP ADDRESS", command=find_ip)
button_ip.pack()
button_ip = Button(root, text="Copy Ip🔎", command=copy_code1, background="Cyan")
button_ip.pack()
#???

root.mainloop()