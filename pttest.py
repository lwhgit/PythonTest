def pt2time(str):
    cnt = 0
    result = ""
    idx = [0,0,0]
    idx[0] = str.find('H')
    idx[1] = str.find('M')
    idx[2] = str.find('S')
    d = str.replace("PT", "").replace('M', 'H').replace('S', 'H').split('H')
    if (idx[0] != -1):
        result = result + d[cnt]
        cnt += 1
    if (idx[1] != -1):
        if (len(d[cnt]) == 1):
            d[cnt] = "0" + d[cnt]
        result = result + ':' + d[cnt]
        cnt += 1
    elif (cnt != 0):
        result = result + ":00"
    if (idx[2] != -1):
        if (len(d[cnt]) == 1):
            d[cnt] = "0" + d[cnt]
        result = result + ':' + d[cnt]
    elif (cnt != 0):
        result = result + ":00"
    return result
    
print(pt2time("PT1H3M5S"))