# Project Title

Generate continuous pure audio tone (fixed frequency) based on varying value from a log file.

## Getting Started

To clone or download use

``` git clone git@github.com:SciTechDude/VaryAudioOnLogChange.git```

Or Use  
`https://github.com/SciTechDude/VaryAudioOnLogChange.git`

### Prerequisites

Need following external python modules
* pyaudio
* numpy
 
## Description

While working with OP at stackoverflow to solve an interesting problem.
OP needed a solution that will generate continuous pure audio tone that varies with change in log value.
After much research , trial and error a solution was deviced based on following `pyaudio`

Pyaudio provides a non-blocking callback method that allows real-time manipulation of audio stream.
The audio stream callback function gets new value value if its received by probing log file
The new value then generates a different audio tone thats related to log value.
The new frequency/tone is then converted to stream using `numpy` and fed into `PyAudio`

The audio tone is popping / cracking free that usually occurs when mixing two audio tones/frequencies mid-stream.

## Authors

* **Anil Mandra** - *Initial work* - [SciTechDude](https://github.com/scitechdude)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Inspiration](https://stackoverflow.com/questions/31384138/how-to-change-continuously-the-frequency-of-a-sinusoidal-sound)
