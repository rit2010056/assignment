# !/usr/bin/python
from Hotal_Avail import HotelAvailabilty
import argparse
import os.path
import datetime

class CommandLine(object):

	def validate_date_format(self, date_text):
	    try:
	        datetime.datetime.strptime(date_text, '%Y-%m-%d')
	        return True
	    except ValueError:
	        return False

	# Function To Parse the argument
	def parse(self):
		parser = argparse.ArgumentParser(description='Hotal Availabilty')
		parser.add_argument('-ho','--hotels', help='Input hotal availabilty csv file path',required=True)
		parser.add_argument('-b','--bookings', help='Input hotal booking csv file path',required=True)
		parser.add_argument('-c','--checkin', help='Input checkin time',required=True)
		parser.add_argument('-ch','--checkout', help='Input checkout time',required=True)
		args = parser.parse_args()
		return args

	# Function To Check Argument value recieved from terminal
	def check_argument(self,args):
		Error = False
		if not os.path.isfile(args.hotels):
			print "- Hotel File is not FOUND"
			Error = True

		if not os.path.isfile(args.bookings):
			print "- Hotel booking File is not FOUND"
			Error = True

		if not self.validate_date_format(args.checkin):
			print "Incorrect checkin data format, should be YYYY-MM-DD"
			Error = True

		if not self.validate_date_format(args.checkout):
			print "Incorrect checkout  data format, should be YYYY-MM-DD"
			Error = True

		if args.checkin>args.checkout:
			print "- Check in date should be less then Check out date"
			Error = True

		# Can Add Date Format Checker
		return Error


if __name__ == "__main__":
	C = CommandLine()
	args = C.parse()
	Error = C.check_argument(args)

	# Every Argument is in right format
	if not Error:
		checkin = args.checkin
		checkout = args.checkout
		hotel_path = args.hotels
		booking_path = args.bookings
		H = HotelAvailabilty(hotel_path, booking_path)
		available_hotel = H.get_availability(checkin, checkout)
		print "Available Hotels Are"
		print available_hotel


