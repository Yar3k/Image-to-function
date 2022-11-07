import functions
import cv2
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog as fd


fileName1 = ""
fileName2 = ""
fileName1Var = ""
fileName2Var = ""

def drawByFileNames():
    global fileName1
    global fileName2
    if fileName1 == "" or fileName2 == "":
        print('suk')
        return
    print('nuu')
    img = functions.image_reader(fileName1)
    img2 = functions.image_reader(fileName2)
    rez = functions.image_hsplit(img, 16)
    rez2 = functions.image_hsplit(img2, 16)
    # idx = 0
    # for r in rez:
    #     cv2.imwrite(str(idx) + "./images/split.png",r)
    #     idx+=1


    arr = functions.arr_rounder(rez)
    arr2 = functions.arr_rounder(rez2)

    dataRed = {'X': list(range(1, len(arr[0])+1)),
            'pav1': arr[0],
            'pav2': arr2[0]
            }  
    dfRed = pd.DataFrame(dataRed)
    dataGreen = {'X': list(range(1, len(arr[1])+1)),
            'pav1': arr[1],
            'pav2': arr2[1]
            }  
    dfGreen = pd.DataFrame(dataGreen)
    dataBlue = {'X': list(range(1, len(arr[2])+1)),
            'pav1': arr[2],
            'pav2': arr2[2]
            }  
    dfBlue = pd.DataFrame(dataBlue)


    root = tk.Tk()


    figureRed = plt.Figure(figsize=(5, 4), dpi=100)
    axRed = figureRed.add_subplot(111)
    lineRed = FigureCanvasTkAgg(figureRed, root)
    lineRed.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    dfRed = dfRed[['X', 'pav1', 'pav2']].groupby('X').sum()
    dfRed.plot(kind='line', legend=True, ax=axRed, color=['r', 'y'], marker='o', fontsize=10)
    axRed.set_title('Raudona')
    
    figureGreen = plt.Figure(figsize=(5, 4), dpi=100)
    axGreen = figureGreen.add_subplot(111)
    lineBlue = FigureCanvasTkAgg(figureGreen, root)
    lineBlue.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    dfGreen = dfGreen[['X', 'pav1', 'pav2']].groupby('X').sum()
    dfGreen.plot(kind='line', legend=True, ax=axGreen, color=['g', 'y'], marker='o', fontsize=10)
    axGreen.set_title('Žalia')

    figureBlue = plt.Figure(figsize=(5, 4), dpi=100)
    axBlue = figureBlue.add_subplot(111)
    lineBlue = FigureCanvasTkAgg(figureBlue, root)
    lineBlue.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    dfBlue = dfBlue[['X', 'pav1', 'pav2']].groupby('X').sum()
    dfBlue.plot(kind='line', legend=True, ax=axBlue, color=['b', 'y'], marker='o', fontsize=10)
    axBlue.set_title('Mėlyna')


    root.mainloop()
    return

def buttonCallback1():
    global fileName1
    fileName1 = fd.askopenfilename()
    print(fileName1)
    global fileName1Var
    fileName1Var.set(fileName1)
    
def buttonCallback2():
    global fileName2
    fileName2 = fd.askopenfilename()
    print(fileName2)
    global fileName2Var
    fileName2Var.set(fileName2)

def main():
    root = tk.Tk()
    global fileName1Var
    global fileName2Var
    fileName1Var = tk.StringVar()
    fileName2Var = tk.StringVar()
    label = tk.Label( root, textvariable=fileName1Var)
    label.place(x=150, y=20)
    label2 = tk.Label( root, textvariable=fileName2Var)
    label2.place(x=150, y=60)

    # Initialize tkinter window with dimensions 300 x 250            
    root.geometry('500x250')    
    
    btnUpload1 = tk.Button(root, text = 'Open image nr 1!', command = buttonCallback1)
    btnUpload1.place(x=20, y=20)
    btnUpload2 = tk.Button(root, text = 'Open image nr 2!', command = buttonCallback2)
    btnUpload2.place(x=20, y=60)
    btn3 = tk.Button(root, text = 'Show charts!', command = drawByFileNames)
    btn3.place(x=20, y=100)
    

    


    root.mainloop()
    return 0

if __name__ == "__main__":
    main()