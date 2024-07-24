from tkinter import Label, Entry, Button, Canvas, PhotoImage,constants


class Widgets(Canvas, Entry,Label,Button):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.entry = Entry()
        self.label = Label()
        self.button = Button()
        self.entry_list =[]
        self.button_list = []
        # self.canvas = Canvas(height=self.height,width=self.width)

    def add_image(self, img, **kwargs):
        """ Takes Image and Canvas Height & Width"""
        height = kwargs['canvas_height']
        width = kwargs['canvas_width']
        self.canvas = Canvas(width=width, height=height)
        self.canvas.create_image(kwargs.get("image_x",height/2), kwargs.get("image_y",width/2), image=img)
        self.canvas.grid(column=kwargs.get('column',0), row=kwargs.get('row',0),columnspan=kwargs.get('columnspan', 1))

    def add_entry(self, **kwargs):
        """ Takes Entry Width """
        column_span = kwargs.get('columnspan', 1)
        insert_text = kwargs.get("insert","")
        self.entry = Entry(width=kwargs['width'],font=('Arial',11))
        self.entry.insert(0, insert_text)
        if kwargs.get('focus',False):
            self.entry.focus()
        self.entry.grid(column=kwargs.get('column',0), row=kwargs.get('row',0) ,columnspan=column_span)
        # return self.entry.get()
        self.entry_list.append(self.entry)

    def get_entry_data(self):
        return self.entry.get()



    def add_label(self,**kwargs):
        """Takes Label Text"""
        defaults = {'column':0,'row':0,'columnspan':1}
        defaults.update(kwargs)
        self.label = Label(text=kwargs['text'],font=kwargs.get('font',('Arial',10)))
        self.label.grid(column =defaults['column'], row= defaults['row'], columnspan = defaults['columnspan'])

    def add_buttons(self,**kwargs):
        """ Takes Button Text and command function"""
        self.button = Button(text= kwargs['text'],width=kwargs.get('width',10),font=kwargs.get('font',('Arial',10)), command=kwargs.get('command',""))
        self.button.grid(column=kwargs.get('column',0), row=kwargs.get('row',0),columnspan=kwargs.get('columnspan', 1))
        self.button_list.append(self.button)


