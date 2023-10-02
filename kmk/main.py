import board

from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP6,board.GP7,board.GP8,board.GP10,board.GP9,board.GP11,
    board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,board.GP18,board.GP19,
    board.GP20,board.GP21,board.GP22,board.GP26,board.GP27,board.GP28
)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
        KC.F6,KC.F7,KC.F8,KC.NOOP,KC.F9,KC.F10,KC.F11,KC.F12,
        KC.PSCREEN,KC.SCROLLLOCK,KC.PAUSE,KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,KC.MEDIA_PLAY_PAUSE,

        KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.EQUAL,KC.N6,KC.BSPACE,
        KC.INSERT,KC.HOME,KC.PGUP,KC.NUMLOCK,KC.KP_SLASH,KC.KP_ASTERISK,

        KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,
        KC.Y,KC.U,KC.I,KC.O,KC.P,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,
        KC.DELETE,KC.END,KC.PGDOWN,KC.KP_7,KC.KP_8,KC.KP_9,

        KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,
        KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.QUOTE,KC.ENTER,
        KC.KP_PLUS,KC.KP_MINUS,KC.AUDIO_MUTE,KC.KP_4,KC.KP_5,KC.KP_6,

        KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,
        KC.NOOP,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.NOOP,KC.RSHIFT,
        KC.NOOP,KC.UP,KC.NOOP,KC.KP_1,KC.KP_2,KC.KP_3,

        KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.NOOP,KC.MO(1),
        KC.NOOP,KC.NOOP,KC.SPACE,KC.NOOP,KC.RALT,KC.LGUI,KC.APP,KC.RCTRL,
        KC.LEFT,KC.DOWN,KC.RIGHT,KC.KP_0,KC.KP_DOT,KC.KP_ENTER
    ],
    [
        KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
        KC.F6,KC.F7,KC.F8,KC.NOOP,KC.F9,KC.F10,KC.F11,KC.F12,
        KC.PSCREEN,KC.SCROLLLOCK,KC.PAUSE,KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,KC.MEDIA_PLAY_PAUSE,

        KC.GRAVE,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.EQUAL,KC.N6,KC.BSPACE,
        KC.INSERT,KC.HOME,KC.PGUP,KC.NUMLOCK,KC.KP_SLASH,KC.KP_ASTERISK,

        KC.TAB,KC.P,KC.O,KC.I,KC.U,KC.Y,
        KC.T,KC.R,KC.E,KC.W,KC.Q,KC.LBRACKET,KC.RBRACKET,KC.BSLASH,
        KC.DELETE,KC.END,KC.PGDOWN,KC.KP_7,KC.KP_8,KC.KP_9,

        KC.CAPS,KC.SCOLON,KC.L,KC.K,KC.J,KC.H,
        KC.G,KC.F,KC.D,KC.S,KC.A,KC.QUOTE,KC.QUOTE,KC.ENTER,
        KC.KP_PLUS,KC.KP_MINUS,KC.AUDIO_MUTE,KC.KP_4,KC.KP_5,KC.KP_6,

        KC.LSHIFT,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,
        KC.NOOP,KC.B,KC.V,KC.C,KC.X,KC.Z,KC.NOOP,KC.RSHIFT,
        KC.NOOP,KC.UP,KC.NOOP,KC.KP_1,KC.KP_2,KC.KP_3,

        KC.LCTRL,KC.LGUI,KC.LALT,KC.SPACE,KC.NOOP,KC.MO(1),
        KC.NOOP,KC.NOOP,KC.SPACE,KC.NOOP,KC.RALT,KC.LGUI,KC.APP,KC.RCTRL,
        KC.LEFT,KC.DOWN,KC.RIGHT,KC.KP_0,KC.KP_DOT,KC.KP_ENTER
    ],
]

keyboard.debug_enabled = True


if __name__ == '__main__':
    keyboard.go()

