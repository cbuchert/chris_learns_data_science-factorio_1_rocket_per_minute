# open a lua file
# parse the lua file to native python
# export a csv
class luaToCsv:
	def open (filePath):
		file = open(filePath, "r")
		return file.read()

	def breakIntoRows (chunk):
		splitDelimiter = "  },\n  {"

		return chunk.split(splitDelimiter)

	# def 

class Recipe:
	def __init__(type, name, enabled, ingredients, energy_required, result, result_count, requester_paste_multiplier):
		super(ClassName, self).__init__()
		self.arg = arg
		self.type = type
		self.name = name
		self.enabled = enabled
		self.ingredients = ingredients
		self.energy_required = energy_required
		self.result = result
		self.result_count = result_count
		self.requester_paste_multiplier = requester_paste_multiplier
		