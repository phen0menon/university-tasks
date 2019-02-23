class DataConverser:
	# Match table
	assoc_table = {
		"A": "0",
		"C": "1",
		"G": "2",
		"T": "3"
	}

	# Convert a symbol to len(self.assoc_table) base
	def convert(self, symbol):
		return self.assoc_table[symbol]

	# Convert a sequence of symbols into a decimal integer
	def convert_to_dec(self, data):
		return int("".join(data), len(self.assoc_table))

	# Set data to convert and return current instance for chaining purpose
	def set_data(self, data):
		self.data = data

		return self

	# Begin conversion (start point)
	def begin(self):
		conversed_data = [self.convert(symbol) for symbol in self.data]
		self.conversed_to_dec = self.convert_to_dec(conversed_data)

		return self

	# Print conversed sequence
	def print(self):
		print(self.conversed_to_dec)


if __name__ == "__main__":
	text = input()

	data_converser = DataConverser()
	data_converser.set_data(text).begin().print()