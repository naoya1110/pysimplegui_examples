import winsound

freqs = {
    "C4":262, # ド
    "D4":294, # レ
    "E4":330, # ミ
    "F4":349, # ファ
    "G4":392, # ソ
    "A4":440, # ラ
    "B4":494, # シ
    "C5":523, # ド
}

duration = 500

for freq in freqs.values():
    winsound.Beep(freq, duration)