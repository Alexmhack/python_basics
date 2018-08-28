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
		for passenger in self.passengers:
			print(f"{passenger.name}")

	def delay(self, duration):
		self.duration += duration
		return self.duration

	def add_passenger(self, p):
		self.passengers.append(p)
		p.flight_id = self.id


class Passenger:
	def __init__(self, name):
		self.name = name


def main():
	f1 = Flight('Indore', 'Delhi', 800)
	alex = Passenger('alex')
	hopper = Passenger('hopper')
	f1.add_passenger(alex)
	f1.add_passenger(hopper)

	f1.print_info()


if __name__ == '__main__':
	main()
