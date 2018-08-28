class Flight:
	def __init__(self, origin, destination, duration):
		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print(f'FLIGHT ORIGIN: {self.origin}')
		print(f'FLIGHT DESTINATION: {self.destination}')
		print(f'FLIGHT DURATION: {self.duration}\n')


def main():
	f = Flight(origin="New York", destination="Paris", duration=500)
	f.print_info()


if __name__ == '__main__':
	main()
