import tkinter

class GraphVisualiser:
    def __init__(self):
        pass
    
    def initialise(self):
        root = tkinter.Tk()
        root.geometry("500x500")
        
        canvas = tkinter.Canvas(root, width=500, height=500, bg="white")
        canvas.pack()
        
        #plot X axis
        
        canvas.create_line(50, 250, 450, 250, width=2, arrow=tk.LAST)
        
        #plot Y axis
        
        canvas.create_line(250, 450, 250, 50, width=2, arrow=tk.LAST)
        
        root.mainloop()
        