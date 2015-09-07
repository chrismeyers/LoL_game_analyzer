import json
import lolapi, summoner
from array import *

class Parser:
	def __init__(self):
		pass

	def getListOfStats(self, data, stat):
		numGames = len(data['games'])
		statsArr = []
		for i in range(0, len(data['games'])):
			statsArr.append(data['games'][i]['stats'][stat])
			print str(i) + ": " + stat + " = " + str(data['games'][i]['stats'][stat])
		return list(reversed(statsArr))
