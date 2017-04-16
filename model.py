
import csv
import operator


data_is_loaded = False

def load_data():
	dg ={}
	gd = {}
	# with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
	# 	reader = csv.DictReader(csvfile, delimiter=',')
	# 	for row in reader:
	# 		pass
		#     if row['state_abbr'] in d:
		#         d[row['state_abbr']].append(float(row['votes_dem_2016']))
		#     else:
		#         d[row['state_abbr']] = [float(row['votes_dem_2016'])]
		#     d1 = dict((key, sum(vals)) for key, vals in d.items())
		#     if row['state_abbr'] in g:
		#         g[row['state_abbr']].append(float(row['votes_gop_2016']))
		#     else:
		#         g[row['state_abbr']] = [float(row['votes_gop_2016'])]
		#     g1 = dict((key, sum(vals)) for key, vals in g.items())
		#data_is_loaded = True

def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	d ={}
	g = {}
	evry = {}
	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row['state_abbr'] != 'AK':
				if row['state_abbr'] in d:
					d[row['state_abbr']].append(float(row['votes_dem_2016']))
				else:
					d[row['state_abbr']] = [float(row['votes_dem_2016'])]
				d1 = dict((key, sum(vals)) for key, vals in d.items())
				sorted_d1 = sorted(d1.items(), key=operator.itemgetter(1))
				order_d1 = sorted(d1.items(), key=operator.itemgetter(0))
			#sorted_d1 = sorted(d1.items(), key=operator.itemgetter(1))
			if row['state_abbr'] != 'AK':

				if row['state_abbr'] in g:
					g[row['state_abbr']].append(float(row['votes_gop_2016']))
				else:
					g[row['state_abbr']] = [float(row['votes_gop_2016'])]
				g1 = dict((key, sum(vals)) for key, vals in g.items())
				sorted_g1 = sorted(g1.items(), key=operator.itemgetter(1))
				sorted_g2 = sorted(g1.items(), key=operator.itemgetter(1,0), reverse = True)

			if row['state_abbr'] != 'AK':
				if row['state_abbr'] in evry:
					evry[row['state_abbr']].append(float(row['total_votes_2016']))
				else:
					evry[row['state_abbr']] = [float(row['total_votes_2016'])]
				evry1 = dict((key, sum(vals)) for key, vals in evry.items())





		if party == 'gop':
			if raw==True:
				if sort_ascending ==True:
					#dem1 = sorted_d1.items()

					return sorted_g1

		if party == 'gop':
			if raw==True:
				if sort_ascending ==False:
					#dem1 = sorted_d1.items()

					return sorted_g2

		if party == 'gop':
			if raw==False:

				if sort_ascending ==True:

					order_g1 = sorted(g1.items(), key=operator.itemgetter(0))
					vall = {k : v / evry1[k] for k, v in g1.items() if k in evry1}
					sorted_vall = sorted(vall.items(), key=operator.itemgetter(1))
					return sorted_vall
						#value = g1[key] * evry[key]

					#vald = sum(g1.values())
		if party == 'gop':
			if raw==False:

				if sort_ascending ==False:

					order_g1 = sorted(g1.items(), key=operator.itemgetter(0))
					vall = {k : v / evry1[k] for k, v in g1.items() if k in evry1}
					sorted_vall2 = sorted(vall.items(), key=operator.itemgetter(1,0), reverse = True)
					return sorted_vall2



					#g1.update((x, (y/vald)) for (x, y) in g1.items())




				# return sorted_g1


		if party == 'dem':
			if raw==True:
				if sort_ascending ==False:
					sorted_d2 = sorted(d1.items(), key=operator.itemgetter(1,0), reverse=True)
					return sorted_d2

		if party == 'dem':
			if raw==True:
				if sort_ascending ==True:
					#dem1 = sorted_d1.items()

					return sorted_d1

		if party == 'dem':
			if raw==False:
				if sort_ascending ==True:
					dall = {k : v / evry1[k] for k, v in d1.items() if k in evry1}
					sorted_dall = sorted(dall.items(), key=operator.itemgetter(1))
					return sorted_dall

		if party == 'dem':
			if raw==False:
				if sort_ascending ==False:
					dall = {k : v / evry1[k] for k, v in d1.items() if k in evry1}
					sorted_dall2 = sorted(dall.items(), key=operator.itemgetter(1,0), reverse=True)
					return sorted_dall2






	# build the appropriate list of tuples to return

	return [('A', 1), ('B', 2)]

#print(get_data())

# def get_sorted_data():
# 	return sorted(get_data(), key=lambda x : x[1], reverse=True)

print (get_data())

if __name__ == "__main__":

	points = 0

	data = get_data()
	#print(data)
	if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
		points += 3.33

	data = get_data(party='gop', raw=False)

	if data [0][0] == 'DC' and int(data[0][1] * 100) == 4 and \
		data[-1][0] == 'WY' and int(data[-1][1] * 100) == 70:
		points += 3.33


	data = get_data(party='dem', raw=True, sort_ascending=False)
	if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
		points += 3.34

	print("points :", points)
