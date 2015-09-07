import tkinter as tk
from tkinter import messagebox
from lib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Gui:
	DEBUG = False
	lastRegion = ""
	lastSummoner = ""
	stats = ""
	mainGUI = tk.Tk()
	mainGUI.resizable(0,0) # Makes GUI unresizable

	api = lolapi.LOLAPI()
	parse = parser.Parser()
	summ = summoner.Summoner()

	title = "League of Legends Recent Game Analyzer"
	if DEBUG:
		title += " [DEBUG]"
	
	mainGUI.title(title)
	mainGUI.geometry("800x700")

	def __init__(self):
		pass
		
	def setupGUI(self):
		#==============FRAMES=============
		app = tk.Frame(self.mainGUI)
		app.pack()
		info = tk.Frame(app)
		info.pack(side=tk.TOP)
		graph = tk.Frame(app)
		graph.pack(side=tk.BOTTOM)

		#===============MENU===============
		menubar = tk.Menu(self.mainGUI)
		menubar.add_command(label="Quit", command=self.mainGUI.quit)
		self.mainGUI.config(menu=menubar)

		#===============NAME===============
		tk.Label(info, text="Summoner Name:").pack(padx=2, pady=10, side=tk.LEFT)
		name = tk.Entry(info)
		name.pack(padx=2, pady=10, side=tk.LEFT)

		#=========REGION SELECTION=========
		tk.Label(info, text="Region:").pack(padx=2, pady=10, side=tk.LEFT)
		regionChoice = tk.StringVar(info)
		regionChoice.set(staticdata.regions[0])
		regionBox = tk.OptionMenu(info, regionChoice, *staticdata.regions)
		regionBox.pack(padx=2, pady=10, side=tk.LEFT)

		#==========STAT SELECTION=========
		tk.Label(info, text="Stat to Analyze:").pack(padx=2, pady=10, side=tk.LEFT)
		statChoice = tk.StringVar(info)
		statChoice.set(staticdata.stats[0])
		statBox = tk.OptionMenu(info, statChoice, *staticdata.stats)
		statBox.pack(padx=2, pady=10, side=tk.LEFT)

		#=============BUTTON==============
		button = tk.Button(info, text='Analyze', pady=15, width=10, command=lambda: self.onClick( \
			fig, canvas, name, regionChoice, statChoice))
		button.pack(side=tk.LEFT)

		#==============PLOT===============
		fig = Figure(dpi=100)
		canvas = FigureCanvasTkAgg(fig, master=graph)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.BOTTOM)

		toolbar = NavigationToolbar2TkAgg(canvas, graph)
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP)

		self.mainGUI.mainloop()

	def onClick(self, fig, canvas, name, regionChoice, statChoice):
		currentStat = statChoice.get()
		currentStatTrans = staticdata.statTranslations[currentStat]

		if self.DEBUG:
			# If DEBUG mode, use canned data.
			# This reduces the amount of typing and API calls used
			# during testing.
			self.summ.currentName = "Spicy Criticals"
			self.summ.currentRegion = "na"
			self.summ.currentID = 29639505
		else:
			self.summ.currentName = name.get()
			self.summ.currentRegion = regionChoice.get()

		if (self.lastSummoner != self.summ.currentName) or (self.lastRegion != self.summ.currentRegion) or (self.lastSummoner == ""):
			# Only get fresh data if name changed, region changed or it's the first time checked.
			if self.DEBUG:
				self.summ.data = self.api.getTestJSON()
				self.stats = self.parse.getListOfStats(self.summ.data, currentStatTrans)
			else:
				# If the summoner name to ID API call raises a ValueError, that means the summoner
				# name given is invalid.  Prompt the user to try again and return.
				try:
					self.summ.currentID = self.api.getIdFromName(self.summ.currentName, self.summ.currentRegion)
				except ValueError as e:
					messagebox.showerror("Error", e)
					print(e)
					return
				self.summ.data = self.api.getMatches(self.summ.currentID, self.summ.currentRegion)
				self.stats = self.parse.getListOfStats(self.summ.data, currentStatTrans)
		else:
			# Use data from previous API call
			self.stats = self.parse.getListOfStats(self.summ.data, currentStatTrans)

		self.lastSummoner = self.summ.currentName
		self.lastRegion = self.summ.currentRegion
		print(self.summ.currentName + " " +  self.summ.currentRegion + " " + str(self.summ.currentID) + "\n")

		graph = fig.add_subplot(111)
		graph.clear()
		graph.set_xlabel("Previous Games")
		graph.set_ylabel(currentStat)
		graph.plot(self.stats)
		canvas.draw()

def main():
	g = Gui()
	g.setupGUI()

if __name__ == '__main__':
	main()
