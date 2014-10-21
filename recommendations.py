critics = {
        'ming': {
            'lady in the water': 2.5, 
            'snake on a plane': 3.5,
            'just my luck': 3.0,
            'superman return': 3.5,
            'you, me and dupree': 2.5
            },
        'lin': {
            'lady in the water': 3.0,
            'snake on a plane': 4.0,
            'just my luck': 3.5,
            'superman return': 4.0,
            'the night listener': 3.0
            },
        'michael': {
            'lady in the water': 2.5,
            'snake on a plane': 3.0,
            'superman return': 3.5,
            'the night listener': 4.5,
            'just my luck': 4.0
            },
        'mick': {
            'lady in the water': 3.0,
            'snake on a plane': 4.0,
            'just my luck': 2.0,
            'you, me and dupree': 2.0,
            'superman return': 4.0
            }
        }

from math import sqrt

def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: 
            si[item] = 1

    n = len(si)
    # has no common
    if n == 0: return 1

    # sum of all preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # square and sum
    sum1sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2sq = sum([pow(prefs[p2][it], 2) for it in si])
    
    psum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num = psum - (sum1 * sum2 / n)
    den = sqrt((sum1sq - pow(sum1, 2) / n) * (sum2sq - pow(sum2, 2) / n))
    if den == 0: return 0
    return num / den

def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        if other != person:
            sim = similarity(prefs, person, other)
        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                # weighting the mark
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # sum of similarity
                simSums.setdefault(item, 0)
                simSums[item] += sim
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]
    return result

def calculateSimilarItems(prefs, n = 3, similarity = sim_distance):
    # key: item, value: top n matches
    result = {}

    itemPrefs = transformPrefs(prefs)
    for item in itemPrefs:
        result[item] = topMatches(itemPrefs, item, n = n, similarity = similarity)
    return result

def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}

    for (item, rating) in userRatings.items():
        for (similarity, item2) in itemMatch[item]:
            if item2 in userRatings: continue

            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    rankings = [(score / totalSim[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
