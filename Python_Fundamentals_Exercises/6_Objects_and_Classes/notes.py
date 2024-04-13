import sounddevice as sd
import numpy as np
import time

def play_note(note_frequency, duration):
    sampling_rate = 44100  # Samples per second

    # Generate a sine wave for the note
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    note_wave = 0.5 * np.sin(2 * np.pi * note_frequency * t)

    # Play the note
    sd.play(note_wave, samplerate=sampling_rate)
    sd.wait()

# Note frequencies (in Hertz)
note_freqs = [130.82, 146.83, 164.81, 174.61, 196, 220, 246.94, 261.63]

# Duration for each note (in seconds)
note_duration = 1

# Play each note
for note_freq in note_freqs:
    play_note(note_freq, note_duration)
    time.sleep(0.2)  # Add a short delay between notes
