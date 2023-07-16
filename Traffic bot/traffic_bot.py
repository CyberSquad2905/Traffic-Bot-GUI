from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from tkinter import messagebox 
import time
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver




# Create a new window
yt = Tk()
yt.title("Traffic bot Desined by Master In Computer Science  (M.I.C.S)go powred by Cyber Squad")
#yt.iconbitmap('channel.ico')
yt.geometry('900x600') #900  600
yt.resizable(False,False)



# Adding Channel logo
# Create a photo image object
img = Image.open('abc.png')
photo = ImageTk.PhotoImage(img)

# # Display the image using a label widget
image_label = Label(yt, image=photo)
image_label.pack()
image_label.place(x=690,y=100)

# Creating a function for visiting our blogger site.
def blogger_ncse():
    url = "https://nationalcomputerscienceeducation.blogspot.com/2023/02/master-in-computer-science-n.html"
    webbrowser.open_new_tab(url)

# Creating a function for visiting our yt channel
def blogger_ncse_yt():
    url = "https://www.youtube.com/channel/UCus6YVdrI1cFXX7223rzGig"
    webbrowser.open_new_tab(url)

# # Creating a function for chrome.
def start_hack_chrome():
    url = url_entry.get()
    num_views = int(views_entry.get())
    wait_time = int(time_entry.get())
    
    for i in range(num_views):
        # Open a Chrome browser using the ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Navigate to the specified URL
        driver.get(url)

        # Wait for the specified delay time
        time.sleep(wait_time)

        # Refresh the page and wait for the delay time again
        driver.refresh()
        time.sleep(wait_time)

        # Close the browser
        driver.quit()
        
# Creating function for starting proxies
def start_proxies():
 yt = Tk()
 yt.title("Proxies servers creater of selected country.")
 #yt.iconbitmap('channel.ico')
 yt.geometry('600x600') #900  600
 yt.resizable(False,False)
# Exit function

# Creating function for user agents
def user_agents():
 yt = Tk()
 yt.title("Proxies servers creater of selected country.")
 #yt.iconbitmap('channel.ico')
 yt.geometry('600x600') #900  600
 yt.resizable(False,False)    



def exit_app():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response == 1:
        yt.quit()

# ...

# Add a label for the app title
title_label = Label(yt, text="Traffic bot ", font=("times new roman", 30, "bold"), bg="Blue", fg="White").place(x=0, y=0, relwidth=1)#title_label.config(highlightbackground='red')


# Creating label for company name.
company_label = Label(yt, text="Desined by Aditya kumar Mishra", bg='blue', fg='Black', font=("Georgia", 9), borderwidth=3, highlightthickness=1, relief="solid", width=30)
company_label.config(highlightbackground='red')
company_label.pack()
company_label.place(x='350',y='55')# 350 5
company_label.config(width= 30, height= 2)# 30 2


# # Create a label widget with a  Upper border
label = tk.Label(yt, text="", borderwidth=2, highlightbackground="red" ,relief="solid")
label.pack()
label.place(x=70,y=100) #100 30
label.place(height= 270, width= 450) # 270 450




# Set the window background color
yt.configure(bg="lightgray")



# Add a label for the URL section
url_label = Label(yt, text="  U .  R  .  L ",font=('Georgia'),fg='blue',bg='Lightgreen',bd=1, relief="solid")
url_label.place(x=80, y=150) # 80 150

# Add an entry widget for the URL section
url_entry = Entry(yt,text= "Enter your URL",font=('Georgia'),fg='Dark blue',bg='white' )
url_entry.configure(bd=2, highlightcolor='red', highlightbackground='green')
url_entry.place(x=260, y=150) # 260 150

# Label for No. of views.
views_label = Label(yt, text="  No. of views ",font=('Georgia'),fg='Blue',bg='lightgreen',bd=1, relief="solid")
views_label.place(x=80, y=220) # 80 220

# Creating an entry for no. of views.
views_entry = Entry(yt,text= "Enter the no. of views you want",font=('Georgia'),fg='Dark green',bg='white' )
views_entry.configure(bd=2, highlightcolor='red', highlightbackground='green')
views_entry.place(x=260, y=220)# 260 220


# Creating a label for watting time.
time_label = Label(yt, text="  Delay (In sec) ",font=('Georgia'),fg='blue',bg='Lightgreen',bd=1, relief="solid")
time_label.place(x=80 , y= 290) # 80 290


# Creating an entry for Watting for time.
time_entry = Entry(yt,text= ".",font=('Georgia'),fg='Dark green',bg='white' )
time_entry.configure(bd=2, highlightcolor='red', highlightbackground='green')
time_entry.place(x=260, y=285) # 260 285


# Creating a label for selecting browser.
browser_lbl = Label(yt,text= "Please select your browser", font=('Futura'), fg= 'red', bg= "Lightblue") 
browser_lbl.pack()
browser_lbl.place(x= 200,y= 400)# 200 400

# # Create a label widget with a  lower border
label = tk.Label(yt, text="", borderwidth=2, relief="solid")
label.pack()
label.place(x=65,y=389.8)  #65 389.8
label.place(height= 190, width= 800)# 190 800

# Creating Button for starting bot
start_button = Button(yt, text="start", font=("times new roman", 15), bg="Yellow", activebackground="Yellow",command= start_hack_chrome, fg="black", activeforeground="black", cursor="hand2").place(x=350, y=405, width=190, height=45)# 350 405 190 45
#  creating a button for proxy
proxy_button = Button(yt, text="proxy", font=("times new roman", 15), bg="Yellow", activebackground="Yellow",command= start_proxies , fg="black", activeforeground="black", cursor="hand2").place(x=85, y=405, width=190, height=45)# 85 405 190
# creating button for user agents 
user_button = Button(yt, text="user agents", font=("times new roman", 15), bg="Yellow", activebackground="Yellow", fg="black", activeforeground="black", command= user_agents ,cursor="hand2").place(x=660, y=405, width=190, height=45)# 660 405 190 405

# Exit from software
exit_button = Button(yt, text="     Exit    ", font=("times new roman", 15), bg="green", activebackground="Red", command= exit_app , fg="black", activeforeground="black", cursor="hand2").place(x=355, y=530, width=190, height=45)#

#Creating follow on youTube.
yt_button = Button(yt, text="    our youTube  channel    ", font=("times new roman", 15), bg="yellow", foreground= "black", activebackground="red", command= blogger_ncse_yt ,fg="white", activeforeground="black", cursor="hand2").place(x=95, y=530, width=190, height=45)#

# Creating follow me on blogger.
bo_button = Button(yt, text="    Our website    ", font=("times new roman", 15), bg="yellow", foreground= "black", activebackground="orange",command=blogger_ncse, fg="white", activeforeground="black", cursor="hand2").place(x=660, y=530, width=190, height=45)#


# Creating a end label
endtitle_label = Label(yt, text="Traffic bot desined by Master In Computer Science (M.I.C.S) go powred by Cyber Squad", font=("times new roman", 10, "bold"), bg="Blue", fg="White").place(x=0, y=581.3, relwidth=1)#title_label.config(highlightbackground='red')


# Creating setup for pyautogui



# Start the main event loop
yt.mainloop()
# (yt, text="U . R . L", font=('Georgia'), fg='black', bg='red', bd=1, relief="solid')
# Create a proxies server

