import pygame
from epgtypes import *
from event import evchecker
from controls import Controller

class Game:
	_wndsize = (640, 480)
	_bgcolor = RGBTuple(0, 0, 0)
	_caption = "-§DEFAULT§caption-"
	_icon = "-§DEFAULT§caption-"
	_nomadewith = False
	
	__screen = pygame.Surface
	__iconsurface = pygame.Surface
	__sprites = {'__list__': []}
	__controls = {'__list__': []}
	__events = {}
	__api = None
	
	def __init__(self):
		pygame.init()
		pygame.mixer.pre_init()
		pygame.mixer.init()
		self.__screen = pygame.display.set_mode(self._wndsize)
		self.__api = GameAPI(self, self.__screen, self.__sprites)
		self.__screen.fill(self._bgcolor)
		self._setcaption()
		self._seticon()

	def _setcaption(self):
		if self._caption != "-§DEFAULT§caption-":
			if self._nomadewith:
				pygame.display.set_caption(self._caption + " (Made with EasyPygame v1.0.0 by @littlekan233)")
			else:
				pygame.display.set_caption(self._caption)
		elif self._caption == "-§DEFAULT§caption-" and not self._nomadewith:
			pygame.display.set_caption("pygame window (Made with EasyPygame v1.0.0 by @littlekan233)")
	
	def _seticon(self):
		if self._caption != "-§DEFAULT§caption-":
			self.__iconsurface = pygame.image.load(_icon)
			pygame.display.set_icon(self.__iconsurface)
			
	def loadSprite(self, spriteClass, spriteId : str):
		if self.__sprites.has_key(spriteId):
			raise ValueError("Sprite ID \"{}\" already exists.".format(spriteId))
		self.__sprites[spriteId] = spriteClass
		self.__sprites["__list__"].append(spriteClass)
		self.__api = GameAPI(self, self.__sprites, self.__controls)
		
	def loadScript(self, interface):
		interface(self.__api)
		
	def loadController(self, controller : Controller, controllerId : str):
		self.__controls[controllerId] = controller
		self.__controls["__list__"].append(controller)
		self.__api = GameAPI(self, self.__sprites, self.__controls)
		
	def addEvent(self, name, instance):
		self.__events[name] = instance
		
	def _event_process(self, pygevent):
		evchecker(pygevent, evdict)
	
	def internal_quitnow(self):
		pygame.event.post(pygame.event.Event(pygame.QUIT))
		
	def run(self):
		while True:
			self._event_process(pygame.event.get())
			self.__screen.fill(self._bgcolor)
			for sprite in self.__sprites["__list__"]:
				self.__screen.blit(sprite.getSurface(), sprite.getRect())
			if len(self.__controls['__list__']):
				for control in self.__controls['__list__']:
					control.blit(self.__screen)
			pygame.display.flip()

class Sprite:
	# Editable variables
	_image = ""
	_position = Position(0,0)
	_password = "Vm10a05GVXlTblJXYTJScVVteGFWVlpyVlRGWlZteFlaVVYwYWxadFVsaFdWekExWVVaS2RWRnJiRmRTYkVwVVZrY3hTMkZzVGpWUFZFNXFWakZ3ZDFkcVFqQlNWMFowV2tWMFZsSXpRbmRXUlZadlZVZE9WazlJU2sxTmFteHpWWHBDTUdSR2NGUmpNMXBwVFdzd2VWbHVjRkpOUjBaWlducENUMUpWTlZaVWEyTTFVa1p2ZWxwSWFHRlNXRUp3V1d4YVJrMVdWalpTYXpWclRXdGFkMXBGYUU5WFZURklUMVJHV2xZelVYZFVWekZUVmxkRmVscEZOVTVoTW5RMlZsUkNhMk15U1hoVldHUlBVa1phVmxsWE1XOVVSbEYzWVVWT2FtRjZiRmRaVlZwaFZXMUdkR1ZFUmxaTlYwMTRXa1JLVDA1c2IzcGlSa3BUVmxWdk1sZFdZM2hUTWtwSFdqTm9VRk5HU2sxVVZWWktZMnhSZVdGNlFrOU5TR2hWVkZWU2EySlhTbkZWVkVwUFUwVktNRmxzVWxOa01YQlhVVlJDYWxKNlJqQlVhMmhEWWtaV1JWVnVaR2xXZWtGM1dUQmtjMU5GTlVsUmJsSm9Va1pLTTFsV1ZtcE5SMDVJVFZjeFQxTkZTakJYYkZKVFpESktXRmRVUW1wU2VrWnZWR3RvUTJSR2NIRlZibHBoVm14VmQxbHFTbGRXYXpWSlVXMW9WMUpHU2pOWFZscFNUVWRPU0ZKc1ZrOVRSVXB2Vm10U1UyUXhiRmRWVkVKcVVqQmFWbFpYTVRCWlZrbDRVMjVLV0dFeVVsUlpWRVozVTBaV2MyRkdaR2xOYkZwSlZERmtORmxWTUhkT1ZGcFlZbFJHYUZsc1duZGtWbEowVFZkR2FWWnNjSHBXTWpCNFZqSktWMk5HYUZoaVZFWm9WbXBHWVdSR1pITmFSMFpvVW0xNFdWVnRNVzlYYkZsM1YyMDVXRll6VWtoVlZFRjRUbXhTY21OR1drNVNSbHBTVmxaYVZrMVdaRlpQVlZwWFlUTkNUMVJWYUVOVlZscFZVVlJHVkdKSFVrZFViR2hIVjIxS1dHVklRbGhpUmtwMldURmFTbVF4VG5KalJuQm9ZbGRvUlZaWGRGZGpNVkY0Vkd4YVQxZEZjSEJaYkdRMFRteGtXR05ITld4WFIxSTFWRVJDVDAxck9VWmpNMXByVFRCc01sVlVUbHBPUms0MVQxWmthVmRHU25sV1IzUnJVbTFXUjJORmJGUmhlbFpaVld4b1ExVldXblJsUjBaYVZtMTRXRlpYZUZkV1IwWnpVMnhrVm1KWWFHaGFWVnBYVjBVMVZrOVdWazVoTTBKS1ZteGtkMUV4WkhKTlZXUnFVbGhvV0ZWcVRtOWhSbkJIVjJ0a2FtSkhVbnBYYTFwUFlWWktXVkZzY0ZkaVdGSlVWWHBHV21WV1VuVlZiRlpvVFc1b1ZWZFhkR0ZaVmxGNFZtNVNhMU5IVWxCV2JURlRaVlphV0dSRmRGVmlSbXcwVlRKMGIxWXhXWHBoUm1oWFZrVndTRlJ0TVV0VFJUbFhZMFprVTFadVFtOVdhMXBoV1Zac1YxUnJXazlXYlhob1ZXMXpNVlF4YkZWU2JIQk9VbTFTV1ZwRldrOVhiRnB6WTBod1YwMXVVbGhXVjNoaFUwZE9ObUY2UW1sTmFrWjFWbXRrTkZVeVNuUldhMlJxVW14YVZWWnJWVEZaVm14WVpVVjBhbFp0VWxoV1Z6QTFZVVpLZFZGcmJGZFNiRXBVVmtjeFMxWnNXbkZWYkZaWFlrVndXRmRzWkhwTlZscFhXa1pXVkdGNlZuQldiWFJhWld4YVNFNVlaRk5oZWtaNldXdGFWMVpzV2tWVWJrSm9WakJhUkZWV1duSmxWa3BWVldzNVUxSnJWWGhXUm1oM1ltczFSazVWVmxSWFIyaFFXVmQwVm1WV1VuVmpSWEJQVmxSR1NWWXhhSGRVTURGeVYyMDVWVlp0VWxkVVZWcHpZMVpLVlZac2NHeGlWa3BEV2tST1NrNVdTblJXYTFwT1ZteGFXRll3YUVOVlJscHlWMjVLYkZac1NsbFVWbHBMWVRBeFJWWlVTbFppUmtwTVZqSjRZVkl4U2xWaGVqQTk="
	
	# Non-editable variables (System variables)
	__oldpos = Position(-1, -1)
	__surface = None
	__rect = None
	__defpwd = "Vm10a05GVXlTblJXYTJScVVteGFWVlpyVlRGWlZteFlaVVYwYWxadFVsaFdWekExWVVaS2RWRnJiRmRTYkVwVVZrY3hTMkZzVGpWUFZFNXFWakZ3ZDFkcVFqQlNWMFowV2tWMFZsSXpRbmRXUlZadlZVZE9WazlJU2sxTmFteHpWWHBDTUdSR2NGUmpNMXBwVFdzd2VWbHVjRkpOUjBaWlducENUMUpWTlZaVWEyTTFVa1p2ZWxwSWFHRlNXRUp3V1d4YVJrMVdWalpTYXpWclRXdGFkMXBGYUU5WFZURklUMVJHV2xZelVYZFVWekZUVmxkRmVscEZOVTVoTW5RMlZsUkNhMk15U1hoVldHUlBVa1phVmxsWE1XOVVSbEYzWVVWT2FtRjZiRmRaVlZwaFZXMUdkR1ZFUmxaTlYwMTRXa1JLVDA1c2IzcGlSa3BUVmxWdk1sZFdZM2hUTWtwSFdqTm9VRk5HU2sxVVZWWktZMnhSZVdGNlFrOU5TR2hWVkZWU2EySlhTbkZWVkVwUFUwVktNRmxzVWxOa01YQlhVVlJDYWxKNlJqQlVhMmhEWWtaV1JWVnVaR2xXZWtGM1dUQmtjMU5GTlVsUmJsSm9Va1pLTTFsV1ZtcE5SMDVJVFZjeFQxTkZTakJYYkZKVFpESktXRmRVUW1wU2VrWnZWR3RvUTJSR2NIRlZibHBoVm14VmQxbHFTbGRXYXpWSlVXMW9WMUpHU2pOWFZscFNUVWRPU0ZKc1ZrOVRSVXB2Vm10U1UyUXhiRmRWVkVKcVVqQmFWbFpYTVRCWlZrbDRVMjVLV0dFeVVsUlpWRVozVTBaV2MyRkdaR2xOYkZwSlZERmtORmxWTUhkT1ZGcFlZbFJHYUZsc1duZGtWbEowVFZkR2FWWnNjSHBXTWpCNFZqSktWMk5HYUZoaVZFWm9WbXBHWVdSR1pITmFSMFpvVW0xNFdWVnRNVzlYYkZsM1YyMDVXRll6VWtoVlZFRjRUbXhTY21OR1drNVNSbHBTVmxaYVZrMVdaRlpQVlZwWFlUTkNUMVJWYUVOVlZscFZVVlJHVkdKSFVrZFViR2hIVjIxS1dHVklRbGhpUmtwMldURmFTbVF4VG5KalJuQm9ZbGRvUlZaWGRGZGpNVkY0Vkd4YVQxZEZjSEJaYkdRMFRteGtXR05ITld4WFIxSTFWRVJDVDAxck9VWmpNMXByVFRCc01sVlVUbHBPUms0MVQxWmthVmRHU25sV1IzUnJVbTFXUjJORmJGUmhlbFpaVld4b1ExVldXblJsUjBaYVZtMTRXRlpYZUZkV1IwWnpVMnhrVm1KWWFHaGFWVnBYVjBVMVZrOVdWazVoTTBKS1ZteGtkMUV4WkhKTlZXUnFVbGhvV0ZWcVRtOWhSbkJIVjJ0a2FtSkhVbnBYYTFwUFlWWktXVkZzY0ZkaVdGSlVWWHBHV21WV1VuVlZiRlpvVFc1b1ZWZFhkR0ZaVmxGNFZtNVNhMU5IVWxCV2JURlRaVlphV0dSRmRGVmlSbXcwVlRKMGIxWXhXWHBoUm1oWFZrVndTRlJ0TVV0VFJUbFhZMFprVTFadVFtOVdhMXBoV1Zac1YxUnJXazlXYlhob1ZXMXpNVlF4YkZWU2JIQk9VbTFTV1ZwRldrOVhiRnB6WTBod1YwMXVVbGhXVjNoaFUwZE9ObUY2UW1sTmFrWjFWbXRrTkZVeVNuUldhMlJxVW14YVZWWnJWVEZaVm14WVpVVjBhbFp0VWxoV1Z6QTFZVVpLZFZGcmJGZFNiRXBVVmtjeFMxWnNXbkZWYkZaWFlrVndXRmRzWkhwTlZscFhXa1pXVkdGNlZuQldiWFJhWld4YVNFNVlaRk5oZWtaNldXdGFWMVpzV2tWVWJrSm9WakJhUkZWV1duSmxWa3BWVldzNVUxSnJWWGhXUm1oM1ltczFSazVWVmxSWFIyaFFXVmQwVm1WV1VuVmpSWEJQVmxSR1NWWXhhSGRVTURGeVYyMDVWVlp0VWxkVVZWcHpZMVpLVlZac2NHeGlWa3BEV2tST1NrNVdTblJXYTFwT1ZteGFXRll3YUVOVlJscHlWMjVLYkZac1NsbFVWbHBMWVRBeFJWWlVTbFppUmtwTVZqSjRZVkl4U2xWaGVqQTk="
	
	# System method
	def __init__(self):
		self.__initSprite()
		self._onCreate()
		
	def __initSprite(self):
		self.__surface = pygame.image.load(self._image)
		self.__rect = self.__surface.get_rect()
		self.__rect.x = self._position[0]
		self.__rect.y = self._position[1]

	# Events
	def _onCreate(self):
		pass
	def _onShow(self):
		pass
	def _onHide(self):
		pass
		
	# Public methods
	def move(self, position : Position):
		self.__rect.x += self._position[0]
		self.__rect.y += self._position[1]

	def getPos(self, password):
		if self._password == self.__defpwd or password != self._password:
			return None
		return self._position

	def setPos(self, position : Position):
		self.__rect.x = self._position[0]
		self.__rect.y = self._position[1]

	def hide(self):
		self.__oldpos = self._position[:]
		self._position = (-999, -999)
		self.__rect.setpos(self._position)
		self._onHide()
		
	def show(self):
		self._position = self.__oldpos[:]
		self.__rect.move(self._position)
		self._onShow()
		
	def getRect(self):
		return self.__rect
	
	def getSurface(self):
		return self.__surface
		
class Script:
	_api = None
	def __init__(self, api):
		self._api = api
		self._ready()
	def _ready(self):
		pass
	# Loop commented because it is optional
	# def loop(self, count):
	# 	pass
		
class GameAPI:
	__game = None
	__screen = None
	__sprites = {}
	__controls = {}
	def __init__(self, gameobj, screen, spritedict, controldict):
		self.__game = gameobj
		self.__screen = screen
		self.__sprites = spritedict
		self.__controls = controldict
	def getSprite(self, id):
		if self.__sprites.has_key(id):
			return self.__sprites[id]
		return None
	def getGame(self):
		return self.__game
	def getScreen(self):
		return self.__screen
	def getController(self, id):
		if self.__controls.has_key(id):
			return self.__controls[id]
		return None
	def finish(self, forcequit = False, forcequitcode = 1):
		if forcequit:
			sys.exit(forcequitcode)
		self.__game.internal_quitnow()
			