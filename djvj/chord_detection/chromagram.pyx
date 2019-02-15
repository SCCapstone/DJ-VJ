# distutils: language = c++
# distutils: sources = djvj/chord_detection/chromagramc.cpp

from libcpp.vector cimport vector
from libcpp cimport bool
from cpython cimport array

cdef extern from "Chromagramc.h":
  cdef cppclass Chromagram:
    Chromagram(int frameSize, int fs) except +
    # void processAudioFrame(double* inputAudioFrame)
    void processAudioFrame(vector[double] inputAudioFrame)
    void setChromaCalculationInterval(int numSamples)
    vector[double] getChromagram()
    bool isReady()

cdef class PyChromagram:
  cdef Chromagram *chromagram

  def __cinit__(self, int frameSize, int fs):
    self.chromagram = new Chromagram(frameSize, fs)

  def __dealloc__(self):
    del self.chromagram

  def processAudioFrame(self, inputAudioFrame):
    return self.chromagram.processAudioFrame(inputAudioFrame)

  def setChromaCalculationInterval (self, numSamples):
    return self.chromagram.setChromaCalculationInterval(numSamples)

  def getChromagram(self):
    return self.chromagram.getChromagram()

  def isReady(self):
    return self.chromagram.isReady()
