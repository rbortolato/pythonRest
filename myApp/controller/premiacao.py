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
            minIntervalAux = res['ano'] - resultDict[res['produtor']]['ano'][lenght-2]
            maxIntervalAux = res['ano'] - resultDict[res['produtor']]['ano'][0]

            if not resultDict[res['produtor']].get('minInterval'):
                resultDict[res['produtor']]['minInterval'] = minIntervalAux
                resultDict[res['produtor']]['minPreviousWin'] = resultDict[res['produtor']]['ano'][lenght-2]
                resultDict[res['produtor']]['minFollowingWin'] = res['ano']
                resultDict[res['produtor']]['maxInterval'] = maxIntervalAux
                resultDict[res['produtor']]['maxPreviousWin'] = resultDict[res['produtor']]['ano'][0]
                resultDict[res['produtor']]['maxFollowingWin'] = res['ano']
            else:
                if minIntervalAux < resultDict[res['produtor']]['minInterval']:
                    resultDict[res['produtor']]['minInterval'] = minIntervalAux
                    resultDict[res['produtor']]['minPreviousWin'] = resultDict[res['produtor']]['ano'][lenght-2]
                    resultDict[res['produtor']]['minFollowingWin'] = res['ano']
                
                if maxIntervalAux > resultDict[res['produtor']]['maxInterval']:
                    resultDict[res['produtor']]['maxInterval'] = maxIntervalAux
                    resultDict[res['produtor']]['maxPreviousWin'] = resultDict[res['produtor']]['ano'][0]
                    resultDict[res['produtor']]['maxFollowingWin'] = res['ano']

            if minInterval == None or minInterval > minIntervalAux:
                minInterval = minIntervalAux
            
            if maxInterval == None or maxInterval < maxIntervalAux:
                maxInterval = maxIntervalAux
    
    retDict = {'max':[], 'min': []}
    
    for k in resultDict:
        if resultDict[k]['minInterval'] == minInterval:
            retDict['min'].append({'producer': k, 'interval': minInterval, 'previousWin': resultDict[k]['minPreviousWin'], 'followingWin': resultDict[k]['minFollowingWin']})

        if resultDict[k]['maxInterval'] == maxInterval:
            retDict['max'].append({'producer': k, 'interval': maxInterval, 'previousWin': resultDict[k]['maxPreviousWin'], 'followingWin': resultDict[k]['maxFollowingWin']})
    
    return retDict