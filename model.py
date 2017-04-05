
import csv

data_is_loaded = False

def load_data():

	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter=',')
	    for row in reader:
	    	pass # process the data
	    data_is_loaded = True

def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	if not data_is_loaded:
		load_data()

	# build the appropriate list of tuples to return

	return [('A', 1), ('B', 2)] 

if __name__ == "__main__":

	points = 0

	data = get_data()
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
