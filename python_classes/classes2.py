class Flight:
	def __init__(self, origin, destination, duration):
		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print(f'FLIGHT ORIGIN: {self.origin}')
		print(f'FLIGHT DESTINATION: {self.destination}')
		print(f'FLIGHT DURATION: {self.duration}\n')

	def delay(self, duration):
		self.duration += duration
		return self.duration


def main():
	f1 = Flight('Indore', 'Delhi', 800)
	f1.print_info()

	f2 = Flight('Mumbai', 'Goa', 800)
	f2.print_info()
	f2.delay(60)


if __name__ == '__main__':
	main()
