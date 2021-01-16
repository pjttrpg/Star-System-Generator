import tkinter as tk
import random
import math

window = tk.Tk()   
window.minsize(650,100)

button1 = tk.Button(
    text = "PLAY GOD",
    fg = "white",
    bg = "black",
    width = 20,
    height = 5
    )

def handle_click(event):
    output.delete(1.0,tk.END)
    getMegaText()
 
output = tk.Text(window, height=10, width=30)

button1.bind("<Button-1>", handle_click)

def getMegaText():
    tagnum = random.randint(0,23)
    caltag = random.randint(0,34)
    nametags = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi",
                "Psi", "Omega"]
    callsigns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",  
                 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    stars = random.randint(0,2)
    age = random.randint(0,21)
    startypes = ["Red Dwarf", "Yellow Dwarf", "Orange Dwarf", "Blue Dwarf", "White Dwarf", "Protostar", "Blue Main-Sequence Star", "Yellow Main-Sequence Star",
             "Orange Main-Sequence Star", "Red Main-Sequence Star", "Red Giant", "Yellow Giant", "Blue Giant", "Blue Supergiant", "Yellow Supergiant", "Red Supergiant", "Blue Hypergiant",
              "Red Hypergiant", "Neutron Star", "Pulsar", "Magnetar", "Black Hole", "Quasar"]
    planets = random.randint(0,6)
    biospheres = ["Tidally Locked Planet", "Cthonian Planet", "Desert Planet", "Gas Dwarf", "Gas Giant", "Ice Giant", "Ice Planet", "Ocean Planet", "Earth-Like Planet", "Failed Star", "Eccentric Orbit Planet",
              "Dwarf Planet", "Rocky Planet", "Greenhouse Planet", "Extreme Conditions Planet"]

    sysname = nametags[random.randint(0,23)] + "-" + callsigns[random.randint(0,34)] + callsigns[random.randint(0,34)] + callsigns[random.randint(0,34)]

    if stars == 0: starcount = "-Unary: " + startypes[random.randint(0,21)] + "."
    if stars == 1: starcount = "-Binary: " + startypes[random.randint(0,21)] + ", " + startypes[random.randint(0,21)] + "."
    if stars == 2: starcount = "-Trinary: " + startypes[random.randint(0,21)] + ", " + startypes[random.randint(0,21)] + ", " + startypes[random.randint(0,21)] + "."

    if planets == 0: bodies = "-This system has no planets."
    if planets == 1: bodies = "-Bodies: " + biospheres[random.randint(0,14)] +"."
    if planets == 2: bodies = "-Bodies: " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + "."
    if planets == 3: bodies = "-Bodies: " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ". " 
    if planets == 4: bodies = "-Bodies: " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + "."
    if planets == 5: bodies = "-Bodies: " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + "."
    if planets == 6: bodies = "-Bodies: " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + ", " + biospheres[random.randint(0,14)] + "."

    output.insert(tk.END, str(sysname)+"\n"+str(starcount)+"\n"+str(bodies))

    output.update_idletasks

output.pack()
output.pack(fill=tk.BOTH, expand=True)
button1.pack()
button1.pack(fill=tk.BOTH, expand=True)
window.mainloop()

