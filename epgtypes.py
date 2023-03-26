class Position:
	__value = []
# Deprecated (make return position list failed)
#	def __init__(self, x : float, y : float):
#		self.__value = [x, y]
	def __new__(self, x : float, y : float):
		self.__value = [x, y]
		return self.__value
	def __mul__(self, k : float):
		return [a * k for a in self.__value]
	def __rmul__(self, k : float):
		return [a * k for a in self.__value]
	def __add__(self, k):
		ret = []
		for a in self.__value:
			for b in k:
				ret.append(a * b)
		return ret
# Deprecated (useless and not working)
# Lazy to delete
#	def __str__(self):
#		return "EasyPygameClass<Position>:[x=3;y=5]"
class RGBTuple:
	def __new__(self, red, green, blue):
		return (red, green, blue)