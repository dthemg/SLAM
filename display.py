import os
dll_path = os.path.abspath(os.path.join(os.getcwd(), "env", 
                "Lib", "site-packages", "sdl2"))
os.environ["PYSDL2_DLL_PATH"] = dll_path
import sdl2
import sdl2.ext  

class Display:
    def __init__(self, W, H):
        sdl2.ext.init()

        self.W, self.H = W, H
        self.window = sdl2.ext.Window("SLAM", size=(W,H), position=(100,100))
        self.window.show()

    def paint(self, img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        surf = sdl2.ext.pixels3d(self.window.get_surface())
        surf[:,:,0:3] = img.swapaxes(0,1)
        self.window.refresh()
