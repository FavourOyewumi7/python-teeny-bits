class Shirt:

	def __init__ (self, color, size, price, style):
		self.color = color
		self.size = size
		self.price = price
		self.style = style
	def calculate_total(self, quantity):
		self.total = self.price * quantity
		return self.total
	def calculate_discount(self, discount):
		count = (1-discount) * self.total
		return count
	def full_descr(self):
		return('You have just bought a {} {} shirt, which is {} and costs {}'.format(self.color, self.style, self.size, self.price))
