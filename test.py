import recommendations

print "distance"
print recommendations.sim_distance(recommendations.critics, 'ming', 'lin')
print recommendations.sim_distance(recommendations.critics, 'ming', 'michael')
print recommendations.sim_distance(recommendations.critics, 'ming', 'mick')

print "pearson"
print recommendations.sim_pearson(recommendations.critics, 'ming', 'lin')
print recommendations.sim_pearson(recommendations.critics, 'ming', 'michael')
print recommendations.sim_pearson(recommendations.critics, 'ming', 'mick')

print "top match"
print recommendations.topMatches(recommendations.critics, 'ming', n = 3)

print "recommendation"
print recommendations.getRecommendations(recommendations.critics, 'ming')

print "recommend items"
items = recommendations.transformPrefs(recommendations.critics)
print recommendations.topMatches(items, 'lady in the water', n =3)
print recommendations.sim_pearson(items, 'lady in the water', 'snake on a plane')

print "item similarity use distance"
print recommendations.calculateSimilarItems(recommendations.critics)

print 'item similarity use pearson'
print recommendations.calculateSimilarItems(recommendations.critics, similarity = recommendations.sim_pearson)

print 'recommendation base on items'
itemsim = recommendations.calculateSimilarItems(recommendations.critics)
print recommendations.getRecommendedItems(recommendations.critics, itemsim, 'ming')
