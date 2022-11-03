from control.connectDB import connectDB

class cursorDB(connectDB):
    def __init__(self):
        super().__init__()
        print('class cursor')
        self.mycursor = self.myconnect.cursor()
        