input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Bitte Warten")
    basic.showString("Dateien werden Exportiert ")
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
    basic.showLeds(`
        # # # . .
        # . # # #
        # . . . #
        # . . . #
        # # # # #
        `)
    basic.showIcon(IconNames.Yes)
    music.setVolume(103)
    basic.showString("Ihre Daten wurden auf Server 1 Übertragen")
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("Keine Verbindung mit dem Server möglich")
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("Lade datei ...")
    basic.pause(100)
    music.playMelody("C C5 C C5 G C5 C C5 ", 170)
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    basic.showString("Aktualisierung ...")
    basic.showLeds(`
        . . # . .
        . # # . .
        # . # . .
        . . # . .
        . . # . .
        `)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.Square)
})
music.playMelody("C5 - C5 C C - - - ", 320)
basic.showString("Server startet")
basic.showLeds(`
    . # # # .
    # # . # #
    # . # . #
    # # . # #
    . # # # .
    `)
radio.sendValue("Proxi", 0)
basic.forever(function on_forever() {
    basic.showLeds(`
        . . # . #
        . # # . #
        # . # . #
        . . # . #
        . . # . #
        `)
    basic.showString("Neue entwicklung finden sie bald in Server 2")
})
basic.forever(function on_forever2() {
    basic.showString("Sie sind noch mit Server ")
    basic.showNumber(1)
    basic.pause(100)
    basic.showString("verbunden")
    basic.pause(100)
    basic.showString("Wenn sie musik Hören wollen schalten sie den Radio oder drücken sie die Tasten A+B gleichzeitig")
    basic.showString("Viel spass ")
    basic.showString("Wünscht ihnen Server 1")
    basic.clearScreen()
})
