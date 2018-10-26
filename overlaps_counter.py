import datetime
import pprint
import numpy
import time
import datetime

d = datetime.date(2018,1,1)
zero = int(d.strftime("%s"))
now = (time.time()) 


seconds = (now - zero) 
# print("zero = " + str(zero))
# print("now = " + str(now))
# print("seconds = " + str(seconds))

FILE = "casy-etoro-6M.txt"
lines = open(FILE).read().split("\n")

time_array = numpy.zeros(int(seconds))

for idx,line in enumerate(lines):
	dat = datetime.datetime.strptime(line, "%d/%m/%Y %H:%M:%S")
	time = int(dat.strftime("%s"))
	if idx%2 == 0:
		start_time = time
	else:
		end_time = time
		time_array[start_time-zero:end_time-zero] += 1


maximum = numpy.argmax(time_array)
print(str(maximum))
maximum = numpy.amax(time_array)
print(str(maximum))

	
histogram = numpy.zeros(20)
casy_histogram = numpy.zeros(20)

last_x = 0
for x in time_array:
	casy_histogram[int(x)] += 1
	if x != last_x:
		histogram[int(x)] += 1
		last_x = x
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(histogram)
print(numpy.sum(histogram[:]))
pp.pprint(casy_histogram)





# isOverlapping =  ((A <= D) && (C <= B) );


# A       B
    # C      D

# s = "2010-01-01 18:48:14.631829"
# datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")

# 15/10/2018 12:03:48
# datetime.datetime.strptime(s, "%d/%m/%Y %H:%M:%S")



# A -> 1Start
# B -> 1End
# C -> 2Start
# D -> 2End

