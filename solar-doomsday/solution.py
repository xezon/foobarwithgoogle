from math import sqrt

def solution(area):
    panelSizes = []
    areaLeft = area

    while areaLeft != 0:
        fittingPanelSize = int(sqrt(areaLeft)) ** 2
        areaLeft -= fittingPanelSize
        panelSizes.append(fittingPanelSize)

    return panelSizes
