print("Starting1")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.col_pins = (board.GP6,board.GP7,board.GP8,board.GP10,board.GP9,board.GP11)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
     KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5, 
     KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,
     KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,
     KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,
     KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.NOOP,KC.MO(1)],
    [KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
     KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5, 
     KC.TAB,KC.P,KC.O,KC.I,KC.U,KC.Y,
     KC.CAPS,KC.SCOLON,KC.L,KC.K,KC.J,KC.H,
     KC.LSHIFT,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,
     KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.NOOP,KC.MO(1)],
]

keyboard.debug_enabled = True


if __name__ == '__main__':
    keyboard.go()

