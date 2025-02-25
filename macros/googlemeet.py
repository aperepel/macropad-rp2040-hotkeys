# Google Meet Hotkeys (MacOS)

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Google Meet', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x200000, keyconfig.KEY_MUTE, [[ConsumerControlCode.MUTE]]),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (0xFF0000, 'Leave', [Keycode.COMMAND, Keycode.W]),
        # 3rd row ----------
        (0x000754, 'People', [Keycode.CONTROL, Keycode.COMMAND, Keycode.P]),
        (0x000754, 'Chat', [Keycode.CONTROL, Keycode.COMMAND, Keycode.C]),
        (0x777777, 'PiP', [Keycode.SHIFT, Keycode.M]),
        # 4th row ----------
        (0x540908, 'Audio', [Keycode.COMMAND, Keycode.D]),
        (0x009900, 'Hand', [Keycode.CONTROL, Keycode.COMMAND, Keycode.H]),
        (0x04541B, 'Video', [Keycode.COMMAND, Keycode.E]),
    ]
}
