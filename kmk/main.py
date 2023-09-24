import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP6,board.GP7,board.GP8,board.GP10,board.GP9,board.GP11,
    board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,board.GP18,board.GP19
)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,  KC.F6,KC.F7,KC.F8,KC.NOOP,KC.F9,KC.F10,KC.F11,KC.F12,
     KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,  KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.EQUAL,KC.N6,KC.BSPACE,
     KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,  KC.Y,KC.U,KC.I,KC.O,KC.P,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,
     KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,  KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.NOOP,KC.ENTER,
     KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B, KC.NOOP,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.NOOP,KC.RSHIFT,
     KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.NOOP,KC.MO(1),  KC.NOOP,KC.NOOP,KC.SPACE,KC.NOOP,KC.RALT,KC.LGUI,KC.APP,KC.RCTRL,
     ],
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

