from ursina import *

import settings
from ui import *


chartEntitys = []
posCache = [
    [],
    [],
    [],
    []
]

chartDatas = []

class Tail(Entity):
    '''
    Hold chart.
    At the back of chart.

    arguments: Bind chart entity(Which chart of back?),Length(UrsinaY.How long is the tail?)
    '''

    def __init__(self,bindChart,length):
        super().__init__()
        self.model = 'quad'
        self.origin_y = 0.5
        self.world_scale = (0.1,length,1)
        self.bindChart = bindChart
        self.position = bindChart.position
        self.isEditing = False
        self.length = length
        self.position = self.bindChart.position
        self.color = bindChart.color
        self.length_unit = self.length/ui.spf
        self.collider = 'box'


    def update(self):
        # print(self.length_unit)

        if self.world_scale_y <= 0.0000001:
            self.world_scale_y = 0.0000001


        self.position = self.bindChart.position


        if self.isEditing:
            self.world_scale_y = -(cameraLine.y - self.y) + mouse.y*-9

        self.length_unit = self.world_scale_y / ui.spf

        if self.intersects(cameraLine.pressChecker).hit:
            PressFlash(self.bindChart.trackID)







class Chart(Entity):
    '''
    Press chart.

    arguments: TrackID(Which track is chart in?),UnitID(Where is chart?),TailLength(UnitID.How long is the tail? Will
    pass to Tail)
    '''
    def __init__(self,unitID,trackID,tailLength=0.0000000001,forceAdd=False,**kwargs):
        super().__init__()

        self.model = 'quad'
        self.scale = (1,0.3,1)
        self.chartPos = [
            0,1,2,3
        ]
        self.color = [color.white,color.gray][trackID%2]

        self.unitID = unitID
        self.trackID = trackID
        self.page = self.unitID // settings.render_range
        self.x = self.chartPos[trackID]
        self.tail = Tail(self,tailLength)
        self.collider = 'box'
        self.y = -ui.spf * self.unitID

        self.chartInfo = ChartInfo(
                            trackId=trackID,
                            page=self.page,
                            unitId=unitID,
                            tailLength=self.tail.length_unit
                        )
        if self.unitID in posCache[self.trackID] and not forceAdd:
            destroy(self.tail)
            destroy(self)
        elif forceAdd:
            chartEntitys.append(self)
            for i in chartDatas:
                if i.unitId == self.unitID and i.trackId == self.trackID:
                    self.chartInfo = i
        else:
            posCache[self.trackID].append(self.unitID)
            chartEntitys.append(self)
            chartDatas.append(
                self.chartInfo
            )

    def update(self):
        self.y = -ui.spf * self.unitID

        if held_keys['right mouse']:
            if mouse.hovered_entity == self:
                self.tail.isEditing = True
        else:
            self.tail.isEditing = False

        self.chartInfo.tailLength = self.tail.length_unit

        if self.intersects(cameraLine.pressChecker).hit:
            PressFlash(self.trackID)

        # print_on_screen(self.chartInfo.tailLength)

    def on_click(self):
        destroy(self.tail)
        destroy(self)
        chartDatas.remove(self.chartInfo)
        chartEntitys.remove(self)
        posCache[self.trackID].remove(self.unitID)
        print(chartDatas)

    def on_destroy(self):
        self.chartInfo.tailLength = self.tail.length_unit





class CameraLine(Entity):
    '''
    Follow camera.

    Editing charts.

    info: Page ID,Absolution
    '''
    def __init__(self):
        super().__init__(
            model='quad',
            scale=(30,0.01,1),
            color=color.blue
        )
        self.unitId = 0
        self.page = self.unitId // settings.render_range

        self.pressChecker = Entity(
            model='cube',
            scale=(30,ui.spf*2,1),
            alpha=0,
            z=-0.1,
            collider='box'
        )
        self.isPlaying = False


        self.lastUnitID = 0



    def update(self):
        if self.unitId < 0:
            self.unitId = 0

        self.y = -ui.spf * self.unitId
        self.page = self.unitId // settings.render_range


        camera.y = self.y
        ui.currentUnitID = self.unitId
        ui.currentPage = self.page

        self.pressChecker.y = self.y

        if cameraLine.unitId != cameraLine.lastUnitID:
            cameraLine.lastUnitID = cameraLine.unitId



    def input(self,event):
        if event == 'scroll up':
            self.unitId -= ui.cameraMoveSpeed
        if event == 'scroll down':
            self.unitId += ui.cameraMoveSpeed


        if event == settings.keys[0]:
            Chart(unitID=self.unitId,trackID=0)
        if event == settings.keys[1]:
            Chart(unitID=self.unitId,trackID=1)
        if event == settings.keys[2]:
            Chart(unitID=self.unitId,trackID=2)
        if event == settings.keys[3]:
            Chart(unitID=self.unitId, trackID=3)


        if event == 'up arrow':
            self.unitId = 0




cameraLine = CameraLine()



class PageLimit(Entity):
    '''
    Limit camera and page.

    argument: Position(Unit ID)
    '''
    def __init__(self):
        super().__init__(
            model='quad',
            scale=(30,0.01,1),
            color=color.red
        )

PageLimit()


class PressFlash(Entity):
    def __init__(self,trackId,**kwargs):
        super().__init__(
            model='quad',
            x=trackId,
            color=color.red,
            scale=(1, 0.3, 1)
        )
        self.aniLast = time.time()

    def update(self):
        if time.time() >= self.aniLast + 1/60:
            self.alpha -= 0.06
            self.aniLast = time.time()

        self.y = cameraLine.y

        if self.alpha <= 0.1:
            destroy(self)
            return


class ChartInfo():
    def __init__(self,trackId,unitId,page,tailLength):
        self.trackId = trackId
        self.unitId = unitId
        self.page = page
        self.tailLength = tailLength #UnitID


def loadCharts(chartJson):

    for trackId in range(4):
        for chart in chartJson['chartFrameIds'][trackId]:
            chartEntitys.append(
                Chart(
                    trackID=trackId,
                    unitID=chart['unitId'],
                    tailLength=chart['tailLengthUnitId']*ui.spf,
                )
            )



