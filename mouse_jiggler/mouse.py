from __future__ import annotations

import ctypes


_user32 = ctypes.WinDLL("user32", use_last_error=True)
_mouse_event = getattr(_user32, "mouse_event")

MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010


def right_click() -> None:
    _mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    _mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)




