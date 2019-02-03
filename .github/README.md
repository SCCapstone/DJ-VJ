# DJ-VJ

DJ-VJ is an easy to use video jockey software that listens to nearby audio input then displays video clips based on the sound it hears, following a set of parameters laid out by the VJ.

## Requirements
- [Python 3.7](https://www.python.org/downloads/release/python-371/)
- [PortAudio](http://www.portaudio.com/)
- [Pipenv](https://pipenv.readthedocs.io)
- Computer audio input set (i.e built-in microphone, USB microphone, etc)

## testing
### Unit Testing
Our unit testing utilizes the [unittest](https://docs.python.org/3/library/unittest.html#) framework    
Unit tests are located in `test/`    

To perform all unit tests:    
    `git clone git@github.com:SCCapstone/DJ-VJ.git`    
    `cd DJ-VJ`    
    `python3 -m unittest discover`    

To perform individual unit test:    
    `git clone git@github.com:SCCapstone/DJ-VJ.git`    
    `cd DJ-VJ`    
    `python3 -m unittest test.<module_name>`    
    ie `python3 -m unittest test.test_freq_to_note`    

### Style Testing
This repo follows the [Pylint](https://www.pylint.org/) style guide. To test adherence to the guide, first download Pylint (`pip install pylint`), then navigate to any python file an execute the command:
`pylint filename.py`, where filename.py is the name of the file you are testing.

## Built With
- [Tkinter](https://wiki.python.org/moin/TkInter) - a Python GUI framework
- [Pickle](https://docs.python.org/3/library/pickle.html) - Python object serialization
- [aubio](https://aubio.org/) - a library for audio and music analysis
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - a cross-platform audio I/O library
- [numpy](https://www.numpy.org/) - package for scientific computing with Python

## Authors
- [Abby Holdeman](https://github.com/aholdeman)
- [Matt Smith](https://github.com/mattsmith803)
- [Joseph Martin](https://github.com/jcm5)
- [Omari Richards](https://github.com/LothropRO)
- [Michael Dyer](https://github.com/TMike1996)
