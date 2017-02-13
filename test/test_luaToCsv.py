import unittest
import sys
sys.path.insert(0, '/vagrant/python_src')
from luaToCsv import luaToCsv
from luaToCsv import Recipe

class testOpenLuaFile (unittest.TestCase):

	def test_actuallyReadsFileContents (self):
		filePath = "/vagrant/test/testFile1.txt"
		file = luaToCsv.open(filePath)
		expectedFileContents = "I'm a different file."

		self.assertEqual(file, expectedFileContents)

class testParseLuaFile (unittest.TestCase):

	def test_recoginzeOutputRows (self):
		sampleData = luaToCsv.open("/vagrant/test/twoTestInputRows.txt")

		self.assertEqual(len(luaToCsv.breakIntoRows(sampleData)), 2)

	def test_buildRecipe (self):
		luaFile = luaToCsv.open("/vagrant/test/twoTestInputRows.txt")
		sampleData = luaToCsv.breakIntoRows(luaFile)[0]

		# TODO: Build the expected recipe for comparison.
		expectedRecipe = Recipe("recipe", "player-port", False, )

		recipe = luaToCsv.buildRecipe(sampleData)

		self.assertEqual(recipe, expectedRecipe)


if __name__	== "__main__":
	unittest.main()
