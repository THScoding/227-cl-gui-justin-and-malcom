import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()
    subprocess.run(command)
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()


root = tk.Tk()
frame = tk.Frame(root)
def run():
 global frame, var
 frame.pack()
 var = 1
 var +=1
 print(var)


# set up button to run the do_command function
# Makes the command button pass it's name to a function using lambd
choices = []
listbox = tk.Listbox(frame, height=4, list=choices)
listbox.insert(0, "ping")
listbox.insert(1, "tracert")
listbox.insert(2, "nslookup")
listbox.insert(3, "netstat")
'''
list.bind("<<ping>>", lambda e: updateDetails(list.curselection()))
list.bind("<Double-1>", lambda e: run(list.curselection()))
'''
listbox.pack()

oneRingBtn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
oneRingBtn.pack()

tracert_btn = tk.Button(frame, text="Check Trace Route", command=lambda:do_command("tracert"))
tracert_btn.pack()

nslookup_btn = tk.Button(frame, text="Nslookup", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

netstat_btn = tk.Button(frame, text="Network Status", command=lambda:do_command("netstat"))
netstat_btn.pack()

save_btn = tk.Button(frame, text="Save", command=lambda:mSave())
save_btn.pack()

  # Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root = tk.Tk()
frame2 = tk.Frame(root)
frame2.pack()

enter_btn = tk.Button(frame2, text="Enter URL",command=run())
enter_btn.pack()

# creates the frame with label for the text box
frame2 = tk.Frame(root, pady=10,  bg="black") # change frame color
frame2.pack()

# decorative label
url_label = tk.Label(frame2, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame2,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

 

root.mainloop()
