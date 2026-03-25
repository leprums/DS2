setcps(0.35)

stack(
    // kick pattern
    s("bd ~ ~ bd ~ bd ~ ~")
        .gain(0.3)
        .lpf(400)
        .room(0.1),

    // snare + ghost hit
    s("~ ~ sd ~ ~ ~ sd ~")
        .gain(0.1)
        .lpf(700)
        .room(0.3),

    // hi-hats groove
    s("hh*8")
        .gain(0.12)
        .lpf(900),

    // перкуссия
    s("~ cp ~ ~ cp ~ ~ ~")
        .gain(0.05)
        .room(0.2),

    // бас
    note("<c2 a1 f1 g1>")
        .sound("sine")
        .slow(2)
        .gain(0.3)
        .lpf(500),

    // аккорды
    note("<c4 e4 g4 b4>*2")
        .sound("triangle")
        .slow(4)
        .room(0.6)
        .gain(0.2),

    // основная мелодия
    note("g4 a4 c5 d5 c5 a4 g4 e4 g4 a4 c5 a4 d5 c5 g4 e4")
        .sound("sine")
        .slow(2)
        .delay(0.3)
        .room(0.6)
        .gain(0.3),

    // верхняя мелодия
    note("~ ~ e5 ~ g5 ~ a5 ~")
        .sound("sin")
        .slow(4)
        .gain(0.18)
        .room(0.7)
)