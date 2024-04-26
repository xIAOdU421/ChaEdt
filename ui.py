from ursina import *
from ursina.prefabs.vec_field import VecField




class UI(WindowPanel):
    def __init__(self):
        super().__init__(
            content=[
                VecField(text='SpeedPerFrame',default_value=0.3),
                VecField(text='Camera move speed',default_value=1.0),
                Text(f'Current unit ID: 0'),
                Text(f'Current page: 0'),
                Button(text='Open'),
                Button(text='Save')
            ]
        )

        self.position = (-0.5, 0.4, 0)

        self.spf = self.content[0].value
        self.cameraMoveSpeed = self.content[1].value
        self.unitIdText = self.content[2]
        self.pageText = self.content[3]
        self.openBtn = self.content[4]
        self.saveBtn = self.content[5]

        # self.goTo = self.content[4].value give up
        # self.goBtn = self.content[5]      give up



        self.currentUnitID = 0
        self.currentPage = 0
    def update(self):
        self.unitIdText.text = f'Current unit ID: {self.currentUnitID}'
        self.pageText.text = f'Current page: {self.currentPage}'

        self.spf = self.content[0].value
        self.cameraMoveSpeed = self.content[1].value






if __name__ == '__main__':
    app = Ursina()
    Hotreload()
    ui = UI()
    app.run()

else:
    ui = UI()




