from myApp.database import execute
def getPremiacao():
    resultList = execute("select * from premiacao where produtor in (select produtor from premiacao group by produtor having count(ano) > 1) order by ano", True)

    resultDict = {}
    minInterval = None
    maxInterval = None
    for res in resultList:
        if not resultDict.get(res['produtor']):
            resultDict[res['produtor']] = {'ano': [res['ano']]}
        else:
            resultDict[res['produtor']]['ano'].append(res['ano'])

            lenght = len(resultDict[res['produtor']]['ano'])
            intervalAux = res['ano'] - resultDict[res['produtor']]['ano'][lenght-2]

            if minInterval == None or minInterval > intervalAux:
                minInterval = intervalAux
            
            if maxInterval == None or maxInterval < intervalAux:
                maxInterval = intervalAux
    
    retDict = {'max':[], 'min': []}
    
    for k in resultDict:
        for x in range(len(resultDict[k]['ano'])):
            if x != 0:
                intervalAux = resultDict[k]['ano'][x] - resultDict[k]['ano'][x-1]

                if intervalAux == minInterval:
                    retDict['min'].append({'producer': k, 'interval': minInterval, 'previousWin': resultDict[k]['ano'][x-1], 'followingWin': resultDict[k]['ano'][x]})

                if intervalAux == maxInterval:
                    retDict['max'].append({'producer': k, 'interval': maxInterval, 'previousWin': resultDict[k]['ano'][x-1], 'followingWin': resultDict[k]['ano'][x]})
    
    return retDict