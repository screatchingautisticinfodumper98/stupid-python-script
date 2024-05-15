import customtkinter
import time
import webbrowser

# this is the chaos of this
def b_chaos():
    scheme1 = customtkinter.CTkLabel(app, text="i see that you've got some balls")
    scheme1.pack(padx =10, pady =10)
    time.sleep(2)
    webbrowser.open("https://discord.gg/JFQqpenKAv")
    time.sleep(12)
    webbrowser.open("https://www.dictionary.com/browse/feet")
    time.sleep(2)
    webbrowser.open("https://open.spotify.com/track/59ndu9VkohItqZDNFYlEYJ?si=44fd76bbfdc24546")
    time.sleep(2)
    print("litterally just made this to see if i could make a window version of a browser tab thingy")

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# the frame of the app
app = customtkinter.CTk()
app.geometry("720, 480")
app.title("the funny time")

# adding ui stuff
title = customtkinter.CTkLabel(app, text="click it i dare you")
title.pack(padx =10, pady =10)

# button
b_start = customtkinter.CTkButton(app, text="do it, trust", command=b_chaos)
b_start.pack(pady =10, padx =10)

app.mainloop()

