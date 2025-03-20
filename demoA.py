from collections import defaultdict
import numpy as np

#-----------------------------------------------------------------------------------------
# Some helper functions.

# Get a random number Generator 
# (old numpy.random functions using a global random number sequence are deprecated).
# Specify a positive integer seed if you want a repeatable sequence of random numbers.
RNG = numpy.random.default_rng(seed = None)

# takes a probability distribution (row of the transition table) and returns the next note
# this took some googling. We'll discuss in more detail after we USE it.
def getNext(probs):
    RNG.random()
    # Your code here.

def playSong(notes):
    # We don't have a music library, so we'll just show the sequence of notes
    print(song)


#-----------------------------------------------------------------------------------------
# Our script to generate MHaLL and a "similar" song from the corresponding Markov chain.

# Rythm of MHaLL.
# fancy list operations! Let's talk about this for a minute
rhythm = [1/4] * 4 + [1/2, 1/2, 1] * 3 + [1/4] * 4 * 3 + [1]  # rhythm of mhall

# The notes for MHaLL (one bar per row).
mhall_notes = [ 'E', 'D', 'C', 'D', 
                'E', 'E', 'E',
                'D', 'D', 'D', 
                'E', 'G', 'G',
                'E', 'D', 'C', 'D', 
                'E', 'E', 'E', 'E',
                'D', 'D', 'E', 'D', 
                'C' ]  

# Play MHaLL.
print("Here is 'Mary had a little lamb':")
playSong(mhall_notes)

# Construct the Markov chain.
# 1) Tally up the transitions from one note to another.
# 1a)   Initialize accumulator.
tallies = defaultdict(lambda: defaultdict(float)) # unpack this! Dictionary of dictionary of floats.
# Why not just a regular old dict()?

# 1b) Write the code to populate tallies!!  Use mhall_notes to create the adjacency / transition matrix.

# 2) Convert tallies table to probability distributions, one per row (think about what you have to do, first).

# 3) Set up uniform distribution table for first note.
# more fancy list operations! (explain zip)
init = dict(zip(tallies.keys(),[1/len(tallies)] * len(tallies)))

# Now we can generate new sequence of notes.
song = [] # set up a song to build

# Your code here! use the getNext  function--what parameter does it expect? how do you specify that parameter?
