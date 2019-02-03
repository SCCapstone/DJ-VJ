Feature: Load Soud File
	Ability to load a wav file and return the correct pitch input

Scenario: Load a sound file and read pitch
	Given program is loaded with a file arguement
	When audio and video are initialized 
	Then the proper video would be played with correct parameters