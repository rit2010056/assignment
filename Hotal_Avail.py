import csv
import datetime
class HotelAvailabilty(object):

	# To Convert String to Date
	def string_to_date(self,date):
		return datetime.date(*map(int, date.strip().split('-')))

	# Constructor to feed data of hotel in dictionary
	def __init__(self):
		self.hotels = {} # 
		with open('metropolis_hotels.csv', 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for hotel in reader:
				self.hotels[hotel[0]] = {}
				self.hotels[hotel[0]]['total'] = int(hotel[1])#Total available room
				self.hotels[hotel[0]]['booked_date'] = {}

		# booked_date key will have all the booked room per date like / {'2015-04-03':3}/
		# means 3 times room has been booked at this date

		with open('metropolis_bookings.csv', 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			for row in reader:
				dictionary = self.hotels[row[0]]['booked_date']
				checkin_date = self.string_to_date(row[1])
				checkout_date = self.string_to_date(row[2])
				self.hotels[row[0]]['booked_date'][checkin_date] = dictionary.get(checkin_date,0)+1
				self.hotels[row[0]]['booked_date'][checkout_date] = dictionary.get(checkout_date,0)+1

			

	#To Get Availabilty
	def get_availability(self,checkin,checkout):
		if checkin>checkout:
			return "Check in date should be less then Check out date"

		checkin = self.string_to_date(checkin)
		checkout = self.string_to_date(checkout)
		available_hotel = []
		for hotel in self.hotels:
			total = self.hotels[hotel]['total']
			total_booked_slot = [] #All number of booked room per date with in the range of checkin and check out
			for booked in self.hotels[hotel]['booked_date']:
				if (booked >= checkin and booked <= checkout):
					total_booked_slot.append(self.hotels[hotel]['booked_date'][booked])

			if total_booked_slot:
				# To Check if any Room is available or not 
				if max(total_booked_slot)<total:
					available_hotel.append(hotel)
			else:
				# If No room is not booked in the range(checkin,checkout) then all room will be available
				available_hotel.append(hotel)
		return available_hotel

H = HotelAvailabilty()
available_hotel = H.get_availability('2015-04-02','2015-05-15')
