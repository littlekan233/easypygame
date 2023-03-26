import pygame

class EPGEvent:
	def __init__(self, gameobj, name):
		self._game = gameobj
		self._name = name
	def __call__(self, func):
		self._game.addEvent(self._name,func)
		def wrapper(event):
			return func(event)
		return wrapper
		
class EPGKeydownEvent(EPGEvent):
	def __init__(self, gameobj):
		super().__init__(gameobj, "keydown")
		
class EPGKeyupEvent(EPGEvent):
	def __init__(self, gameobj):
		super().__init__(gameobj, "keyup")

class EPGQuitEvent(EPGEvent):
	def __init__(self, gameobj):
		super().__init__(gameobj, "quit")
		
def evchecker(self, pygev, evdict):
	for event in pygev:
		if event.type == pygame.QUIT:
			,