import urllib, json
import inspect

class LOLAPI:
	def __init__(self):
		pass

	def getApiKey(self):
		keyFile = open('../notes/key.txt', 'r')
		return keyFile.readlines()

	def buildMatchURL(self, summID, region):
		return "https://" + region + ".api.pvp.net/api/lol/" + region +\
			"/v1.3/game/by-summoner/" + str(summID) + "/recent?api_key=" + str(self.getApiKey()[0])

	def buildSummIdURL(self, name, region):
		return "https://" + region + ".api.pvp.net/api/lol/" + region +\
			"/v1.4/summoner/by-name/" + name + "?api_key=" + self.getApiKey()[0]

	def getIdFromName(self, name, region):
		url = self.buildSummIdURL(name, region)
		data = self.getJSON(url)
		return data[self.formatName(name)]['id']

	def getMatches(self, summID, region):
		url = self.buildMatchURL(summID, region)
		data = self.getJSON(url)
		return data

	def getJSON(self, url):
		print "FRESH DATA, API CALL USED FROM " + str(inspect.stack()[1][0].f_locals["self"].__class__) + \
			  "."  + str(inspect.stack()[1][0].f_code.co_name)
		response = urllib.urlopen(url)
		return json.loads(response.read())

	def getTestJSON(self):
		jsonFile = open('../notes/test.json', 'r')
		return json.loads(jsonFile.read())

	def formatName(self, raw):
		return raw.replace(" ", "").lower()
