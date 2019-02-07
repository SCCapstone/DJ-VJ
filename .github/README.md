# DJ-VJ

DJ-VJ is an easy to use video jockey software that listens to nearby audio input then displays video clips based on the sound it hears, following a set of parameters laid out by the VJ.

## Requirements
- [Python 3.7](https://www.python.org/downloads/release/python-371/)
- [PortAudio](http://www.portaudio.com/)
- [Pipenv](https://pipenv.readthedocs.io)
- Computer audio input set (i.e built-in microphone, USB microphone, etc)

## Virtual Environment
`pipenv install`  
`pipenv run python main.py`  

#### Note
We've been running into issues with the pipenv environment, as it's difficult to hard-install PortAudio, which is necessary for pyaudio to run. If the pipenv file does not work, you can still run our program by running the following commands:  
`pip install aubio`  
`pip install pyaudio (for Mac OSX brew install portaudio then pip install pyaudio, for Linux sudo apt-get portaudio)`  
`pip install open-cv`  
`pip install numpy`  
`python3 main.py`

## Tests
### Unit Testing
Our unit testing utilizes the [unittest](https://docs.python.org/3/library/unittest.html#) framework    
Unit tests are located in `test/`    

To perform all unit tests:    
    `git clone git@github.com:SCCapstone/DJ-VJ.git`    
    `cd DJ-VJ`    
    `python3 -m unittest discover` or `pipenv run python3 -m unittest discover` for virtual environment    

To perform individual unit test:    
    `git clone git@github.com:SCCapstone/DJ-VJ.git`    
    `cd DJ-VJ`    
    `python3 -m unittest test.<module_name>`    
    ie `python3 -m unittest test.test_freq_to_note`    

### Behavioral Testing
To run behavioral test, navigate to the central repository, type `python3 create_screen_behavioral.py` and watch as the program loads, the splash screen is displayed, and the main screen appears.
An example of the test running correctly can be found here: [Video Link](https://www.youtube.com/watch?v=n8oJEo63ybw)

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
