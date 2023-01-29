import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk

from PIL import Image
import os

def alex_to_steve(file, saveas):
    im = Image.open(file).convert('RGBA')
    pixelMap = im.load()
    
    img = Image.new("RGBA", (64, 64))
    pixelsNew = img.load()
    
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            done = False
            
            if 16 <= y <= 35:
                if 47 <= x <= 55:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 45:
                    pixelsNew[x, y] = pixelMap[x, y]
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 46:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
            
            if 36 <= y <= 47:
                if 47 <= x <= 55:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 45:
                    pixelsNew[x, y] = pixelMap[x, y]
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 46:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
            
            if 48 <= y <= 63:
                if 39 <= x <= 47:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if 55 <= x <= 62:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 37:
                    pixelsNew[x, y] = pixelMap[x, y]
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 38:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 53:
                    pixelsNew[x, y] = pixelMap[x, y]
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 54:
                    pixelsNew[x + 1, y] = pixelMap[x, y]
                    done = True
                
                if x == 63:
                    pixelsNew[x, y] = pixelMap[x - 1, y]
                    done = True
            
            if not done:
                pixelsNew[x, y] = pixelMap[x, y]
    
    im.close()
    img.save("temp.png")
    img.close()
    
    im2 = Image.open("temp.png").convert('RGBA')
    pixelMap2 = im2.load()
    
    os.remove("temp.png")
    
    img2 = Image.new("RGBA", (64, 64))
    pixelsNew2 = img2.load()
    
    for x in range(img2.size[0]):
        for y in range(img2.size[1]):
            done = False
            
            if 16 <= y <= 19 or 32 <= y <= 35:
                if x == 50:
                    pixelsNew2[x, y] = pixelMap2[x - 1, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 51:
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
            
            if 48 <= y <= 51:
                if x == 42:
                    pixelsNew2[x, y] = pixelMap2[x - 1, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 43:
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 58:
                    pixelsNew2[x, y] = pixelMap2[x - 1, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 59:
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
            
            if 52 <= y <= 63:
                if x == 46:
                    pixelsNew2[x, y] = pixelMap2[x, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 47:
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 62:
                    pixelsNew2[x, y] = pixelMap2[x, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 63:
                    pixelsNew2[x, y] = pixelMap2[x - 1, y]
                    done = True
            
            if 20 <= y <= 31 or 36 <= y <= 47:
                if x == 53:
                    pixelsNew2[x, y] = pixelMap2[x - 1, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
                
                if x == 55:
                    pixelsNew2[x, y] = pixelMap2[x - 1, y]
                    pixelsNew2[x + 1, y] = pixelMap2[x, y]
                    done = True
            
            if not done:
                pixelsNew2[x, y] = pixelMap2[x, y]
    
    im2.close()
    img2.save(saveas)
    img2.close()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Theme Demo')
        self.geometry('500x400')
        self.style = ttk.Style(self)
        # self.style.theme_use(self.style.theme_names()[1])

        # load button
        self.load_btn = ttk.Button(self, text = 'Load file', command=self.loadFiles)
        self.load_btn.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = 'w')

        # label
        ttk.Label(self, text='Selected:').grid(column=1, row=0, padx=10, pady=10,  sticky='w')

        # entry
        self.load_entry = ttk.Entry(self, width=40)
        self.load_entry.grid(column=1, row=0, padx=75, pady=10,  sticky='w')

        # Drop downs
        OPTIONS = [
            "Steve (4px)", # It has to be there twice because idk it just has ok
            "Steve (4px)",
            "Alex (3px)",
        ]
        # From
        ttk.Label(self, text = 'Convert From:').grid(column = 0, row = 1, padx = 10, pady = 10, sticky = 'w')
        self._from = tk.StringVar(self)
        self._from.set(OPTIONS[0])  # default value
        
        self.from_dropdown = ttk.OptionMenu(self, self._from, *OPTIONS)
        self.from_dropdown.grid(column=1, row=1, padx=10, pady=10,  sticky='w')
        
        # To
        ttk.Label(self, text = 'Convert To:').grid(column = 0, row = 2, padx = 10, pady = 10, sticky = 'w')
        self._to = tk.StringVar(self)
        self._to.set(OPTIONS[0])  # default value

        self.to_dropdown = ttk.OptionMenu(self, self._to, *OPTIONS)
        self.to_dropdown.grid(column = 1, row = 2, padx = 10, pady = 10, sticky = 'w')
        
        # Convert!!
        self.conv_btn = ttk.Button(self, text='Convert', command=self.convert)
        self.conv_btn.grid(column = 0, row = 3, padx = 10, pady = 10, sticky = 'w')

    def convert(self):
        if not os.path.exists(self.load_entry.get()):
            tk.messagebox.showerror("Error!", "Your selected file is invalid")
            return
    
        if self._from.get() != "Alex (3px)" or self._to.get() != "Steve (4px)":
            tk.messagebox.showerror("Error!", "Only Alex to Steve is currently supported.")
            return
        
        filename = asksaveasfilename(title = "Save converted skin", filetypes = (("Minecraft Skins", ".png"),))
        alex_to_steve(self.load_entry.get(), filename)
        tk.messagebox.showinfo("Success!", "Your skin has been converted!")

    def loadFiles(self):
        filename = askopenfilename(title = "Select your skins", filetypes = (("Minecraft Skins", ".png"),))
        self.load_entry.delete(0, tk.END)
        self.load_entry.insert(0, filename)


if __name__ == "__main__":
    app = App()
    app.mainloop()
