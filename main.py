import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        #initialising the window
        super().__init__(parent=None, title='Hello World')
        #declaring the panel, then its corresponding sizer
        panel = wx.Panel(self)        
        sizer = wx.BoxSizer(wx.VERTICAL)
        #the text telling the user to select the file to decode
        infot = wx.StaticText(panel, label="Select the file to decode:")
        sizer.Add(infot, 0, wx.ALL | wx.LEFT, 5)
        #the file picker
        self.filepick = wx.FilePickerCtrl(panel)
        sizer.Add(self.filepick, 0, wx.ALL | wx.EXPAND, 5)
        #the decode button, binded to the catcodec function        
        my_btn = wx.Button(panel, label='Decode')
        my_btn.Bind(wx.EVT_BUTTON, self.start)
        sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(sizer)        
        self.Show()

    def start(self, event):
        value = self.filepick.GetPath()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()