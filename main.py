from ursina import *
import importlib

app = Ursina()
window.borderless = False

# from ui import *
from editor import *
from file import *

song = Audio('MapAssets/song/song.ogg')
playLast = cameraLine.unitId / 200
playLastUnit = 0

song.stop()


lastPage = 0


ui.saveBtn.on_click = save
ui.openBtn.on_click = openCharts


backupLast = time.time()



def update():
    global lastPage
    global backupLast

    if cameraLine.isPlaying:
        cameraLine.pressChecker.collider = 'box'
        cameraLine.pressChecker.visible = True
        cameraLine.unitId = playLastUnit + (time.time() - playLast) * 200
    else:
        cameraLine.pressChecker.collider = None

    if cameraLine.page != lastPage:
        print('page changed!')
        lastPage = cameraLine.page
        clearChart()
        loadChart(cameraLine.page+1)
        loadChart(cameraLine.page)

    if time.time() >= backupLast + 20 and not chartDatas == []:
        save(backup=True)
        backupLast = time.time()




def input(event):
    global playLast
    global playLastUnit
    if event == 'space':
        cameraLine.isPlaying = not cameraLine.isPlaying

        if cameraLine.isPlaying:

            song.play(cameraLine.unitId / 200)
            playLast = time.time()
            playLastUnit = cameraLine.unitId
        else:
            song.stop()



def clearChart():
    for i in chartEntitys:
        # if i.tail.length_unit >= settings.render_range:
        #     pass
        # else:
        destroy(i.tail)
        destroy(i)
        chartEntitys.remove(i)

def loadChart(page):
    for i in chartDatas:
        if i.page == page:
            chartEntitys.append(
                Chart(
                    unitID=i.unitId,
                    trackID=i.trackId,
                    tailLength=i.tailLength*ui.spf,
                    forceAdd=True
                )
            )
    print(f'loaded {len(chartEntitys)} entitys!')



app.run()
