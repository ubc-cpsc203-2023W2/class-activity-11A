
import music as M
from collections import defaultdict
import numpy as np

freq = {
    "C": [16.35, 32.70, 65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01],
    "Db":   [17.32, 34.65, 69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
    "D":   [18.35, 36.71, 73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.64],
    "Eb":   [19.45, 38.89, 77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
    "E":   [20.60, 41.20, 82.41, 164.81, 329.63, 659.26, 1318.51, 2637.02],
    "F":   [21.83, 43.65, 87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83],
    "Gb":   [23.12, 46.25, 92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96],
    "G":   [24.50, 49.00, 98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96],
    "Ab":   [25.96, 51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44],
    "A":   [27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00],
    "Bb":   [29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31],
    "B":   [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07]
}

#  start a ѕynth
b = M.core.Being()

#  set its parameters using sequences representing the song we're modeling
b.fv_ = [1]  # vibrato frequency
b.nu_ = [0]  # vibrato depth in semitones (maximum deviation of pitch)
b.d_ = [1/2] * 4 + [1/2, 1/2, 1] * 3 + [1/2]*4 + [1/2, 1/2, 1] + [1/2] * 4 + [2]  # rhythm of mhall
b.f_ = [freq['E'][4],freq['D'][4],freq['C'][4],freq['D'][4],freq['E'][4],freq['E'][4],freq['E'][4],
        freq['D'][4],freq['D'][4],freq['D'][4],freq['E'][4],freq['G'][4],freq['G'][4],
        freq['E'][4],freq['D'][4],freq['C'][4],freq['D'][4],freq['E'][4],freq['E'][4],freq['E'][4],
        freq['D'][4],freq['D'][4],freq['E'][4],freq['D'][4],freq['C'][4]]  # the notes

#  render the wavfile
b.render(25, 'mhall.wav')

#returns the next note based on given discrete distn
def getNext(probs):
    np.random.seed()
    return np.random.choice(list(probs.keys()), 1, probs.values())[0]

#tally transitions

tallies = defaultdict(lambda: defaultdict(float))
prev = b.f_[0]
for note in b.f_[1:]:
    tallies[prev][note] += 1
    prev = note

print(tallies)
# convert tallies table to probability distribution
for from_note in tallies: # returns a dictionary of tallies for a row
    sum_row = sum(tallies[from_note].values())

    for to_note in tallies[from_note]:
        tallies[from_note][to_note] = tallies[from_note][to_note]/sum_row


# set up uniform distribution table for first note
init = dict(zip(tallies.keys(),[1/len(tallies)] * len(tallies)))
print(init)


# generate new sequence of notes

song = [] # set up a song to build
current = getNext(init) #choose first note!
song.append(current)

#build the song
for note in range(24):
    current = getNext(tallies[current])
    song.append(current)

print (song) #view song data in console for sanity check

#translate from list of numbers to song of notes
new_song = M.core.Being()

# 2) set its parameters using sequences representing the song we're modeling
new_song.fv_ = [1]  # vibrato frequency
new_song.nu_ = [0]  # vibrato depth in semitones (maximum deviation of pitch)
new_song.d_ = b.d_ # same rhythm as MHALL
new_song.f_ = song # our new notes!

# 3) render the wavfile
new_song.render(25, 'new.wav')
