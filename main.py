def on_button_pressed_a():
    basic.show_string("Bitte Warten")
    basic.show_string("Dateien werden Exportiert ")
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    basic.show_leds("""
        # # # . .
        # . # # #
        # . . . #
        # . . . #
        # # # # #
        """)
    basic.show_icon(IconNames.YES)
    music.set_volume(103)
    basic.show_string("Ihre Daten wurden auf Server 1 Übertragen")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("Keine Verbindung mit dem Server möglich")
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_string("Lade datei ...")
    basic.pause(100)
    music.play_melody("C C5 C C5 G C5 C C5 ", 170)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string("Aktualisierung ...")
    basic.show_leds("""
        . . # . .
        . # # . .
        # . # . .
        . . # . .
        . . # . .
        """)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SQUARE)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

music.play_melody("C5 - C5 C C - - - ", 320)
basic.show_string("Server startet")
basic.show_leds("""
    . # # # .
    # # . # #
    # . # . #
    # # . # #
    . # # # .
    """)
radio.send_value("Proxi", 0)

def on_forever():
    basic.show_leds("""
        . . # . #
        . # # . #
        # . # . #
        . . # . #
        . . # . #
        """)
    basic.show_string("Neue entwicklung finden sie bald in Server 2")
basic.forever(on_forever)

def on_forever2():
    basic.show_string("Sie sind noch mit Server ")
    basic.show_number(1)
    basic.pause(100)
    basic.show_string("verbunden")
    basic.pause(100)
    basic.show_string("Wenn sie musik Hören wollen schalten sie den Radio oder drücken sie die Tasten A+B gleichzeitig")
    basic.show_string("Viel spass ")
    basic.show_string("Wünscht ihnen Server 1")
    basic.clear_screen()
basic.forever(on_forever2)
