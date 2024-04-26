import json

import ui

from editor import *
from ui import *
from tkinter.filedialog import *


def save(backup=False):
    print_info('Saving')
    if not backup:
        with open('./MapAssets/charts/chart', 'w') as file:
            json.dump(generateChartDatas(),file,indent=2)

    with open(f'./MapAssets/charts/backups/chart{time.strftime("%Y_%m_%d_%H_%M_%S")}','w') as backup:
        json.dump(generateChartDatas(),backup,indent=2)


def generateChartDatas():
    global chartDatas
    chartFrameIds = [
        [],
        [],
        [],
        []
    ]
    for trackId in range(4):
        for chart in chartDatas:
            print(chart)
            if chart.trackId == trackId:
                chartFrameIds[trackId].append(
                    {
                        'unitId':chart.unitId,
                        'tailLengthUnitId':chart.tailLength
                    }
                )

    saveChartDatas = {
        'songName':'',
        'songAuthor':'',
        'mapAuthor':'',
        'speed': ui.spf,
        'chartFrameIds':chartFrameIds
    }
    return saveChartDatas


def openCharts():
    chartFile = askopenfilename(title='Choice json chart file')

    with open(chartFile,'r') as f:
        chartJson = json.load(f)


    loadCharts(chartJson)