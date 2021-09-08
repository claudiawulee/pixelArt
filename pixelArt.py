import tkinter
def drawPixelArt(root, template, pixelSize, colors):
    lines = template.split("\n")
    #print(lines)
    pWidth = len(lines[0]) * pixelSize
    pHeight = len(lines) * pixelSize
    canvas = makeCanvas(root, pWidth, pHeight)
    lineCount = 0

    for line in lines:
        #print(line)
        charCount = 0
        for char in line:
            #print(char)
            if char != " ":
                char = int(char)
                color = colors[char]
                canvas.create_rectangle(charCount, lineCount ,charCount + pixelSize, lineCount + pixelSize, fill = color, outline="")
            charCount +=pixelSize
        lineCount +=pixelSize


# helper function for drawPixelArt - don't modify
def makeCanvas(root, w, h):
    canvas = tkinter.Canvas(root, width=w, height=h)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    return canvas

def myPixelArt():
    print("Insert your own pixel art here!")
    root = tkinter.Tk()
    pixelSize = 30 # update this!
    colors = ["lime green", "DarkGoldenrod4", "gold4", "forest green"] # update this!
    art = """
                                
                 00
                0000
               000000
              00000000
             3300000033
             3330000333
             1133003322
             1113333222
             1111332222
             1111122222
             1111122222
             1111122222
             1111122222
             1111122222
             1111122222"""
    # tried to draw the minecraft grass block :)
    art = padLines(art) # makes sure all lines are same length
    drawPixelArt(root, art, pixelSize, colors)
    root.mainloop()

def padLines(text):
    lines = text.split("\n")
    length = max(len(line) for line in lines)
    for i in range(len(lines)):
        lines[i] = lines[i] + (length - len(lines[i])) * " "
    return "\n".join(lines)

def runDrawPixelArt():
    print("Running drawPixelArt()...", end="")
    root = tkinter.Tk()
    art1 = padLines("""  0     1     2
 000   111   222
00000 11111 22222
 000   111   222
  0     1     2""")
    drawPixelArt(root, art1, 40, ["blue", "green", "red"])
    root.mainloop()

    root = tkinter.Tk()
    art2 = padLines("""                            0000
        00000000000000000000    00
00000000            0000000000000 00
0 000000000000000000         000000 00
0000                11111    0 0   00 00
00 0        111111111111111110 0   0000 0
 0 000000111111111111111111110 00000 0000
 0 0   0 111111111111111111110 0   0 0
 0 0   0 111111111111111333330 0   0 0
 0 0   0 111111111333422422420 0   0 0
 0 0   0 111113324224224224220 0   0 0
 0 0   0 111324242242242242240 0   0 0
 0 0   0 132422422422422424440 0   0 0
 0 0   0 034224224224444444440 0   0 0
 0 0   0 0 3444444444444444430 0   0 0
 0 0   0 0  344444444444444310 0   0 0
 0 0   0 0   14444444444441  0 0   0 0
 0 0   0 0    114444444431   0 0   0 0
 0 0   0 0       1134111     0 0   0 0
 0 0   0 0         33        0 0   0 0
 0 0   0 0      11143111     0 0   0 0
 0 0   0 0    1111134111111  0 0   0 0
 0 0   0 0   111111331111111 0 0   0 0
 0 0   0 0  111111143111111110 0   0 0
 0 0   0 0 1111111133111111110 0   0 0
 0 0   0 011111111141111111110 0   0 0
 0 0   0 011111111141111111110 0   0 0
 0 0   0 111111113444311111110 0   0 0
 0 0   0 111111134444431111110 0   0 0
 0 0   0 111111344444443111110 0   0 0
 0 0   01111113444444444311110 0   0 0
 0 0 0001111134444444444431110 00000 0000
 0 00   1111344444444444443110 0   000 00
 0 0    1111344444444444444310 0     00 0
00000   0113444444444444444310 0   00  00
0    00000000004444440000    000 00  00
0000000000000  111111  0000000000  00
            00000000000000000000000""")
    drawPixelArt(root, art2, 10, ["black", "blue", "red", "purple", "yellow"])
    root.mainloop()
    print("... done!")

runDrawPixelArt()
myPixelArt()