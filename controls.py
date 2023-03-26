from epgtypes import Position, RGBTuple
from pygame.font import SysFont
from pygame import Rect, Surface
class Controller:
    def __init__(self):
        # Controller init
        pass
    def destroy(self):
        # Destroy controller
        del self
    def blit(screen):
    	# Show controller on screen
    	pass

class Button(Controller):
    def __init__(
		self, 
        #screen : Surface, 
        width : int, 
        height : int, 
        text : str, 
        pos = Position(0,0), 
        color = {
        	'text': RGBTuple(0, 0, 0), 
            'button': RGBTuple(255, 0, 0)
        }, 
        *font : str, 
        size = 12, 
        antialias = True
	):
        #super().__init__()
        if font:
            textshow = SysFont(font, size)
        else:
            textshow = SysFont(None, size)
        rect = Rect(pos[0], pos[1], width, height)
        txtimg = textshow.render(text, antialias, color['text'], color['button'])
        txtrect = txtimg.get_rect()
        txtrect.center = rect.center
	def blit(screen):
		#super().blit()
        screen.fill(color['button'], txtrect)
        screen.blit(txtimg, txtrect)