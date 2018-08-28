class Flight:
	counter = 1

	def __init__(self, origin, destination, duration):
		# Keep track of id number
		self.id = Flight.counter
		Flight.counter += 1

		# Keep track of passengers
		self.passengers = []

		# Details of flight
		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print(f'FLIGHT ORIGIN: {self.origin}')
		print(f'FLIGHT DESTINATION: {self.destination}')
		print(f'FLIGHT DURATION: {self.duration}\n')

		print("PASSENGERS: ")
		for passengers in self.passengers:
			print(f"{passenger.name}")

	def delay(self, duration):
		self.duration += duration
		return self.duration

	def add_passenger(self, p):
		self.passengers.append(p)
		p.flight_id = self.id


def main():
	f1 = Flight('Indore', 'Delhi', 800)
	f1.print_info()

	f2 = Flight('Mumbai', 'Goa', 800)
	f2.print_info()
	f2.delay(60)


if __name__ == '__main__':
	main()
