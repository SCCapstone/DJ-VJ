# distutils: language = c++
# distutils: sources = djvj/chord_detection/ChordDetectorc.cpp

cdef extern from "ChordDetectorc.h":
  cdef cppclass ChordDetector:
    ChordDetector() except +
    void detectChord(double* chroma)
    int rootNotes
    int quality
    int intervals

cdef class PyChordDetection:
  cdef ChordDetector *chord_detection

  def __cinit__(self):
    self.chord_detection = new ChordDetector()

  def __dealloc__(self):
    del self.chord_detection

  def detectChord(self, chroma):
    cdef double c_chroma[12]

    for i in range(len(chroma)):
      c_chroma[i] = chroma[i][0]

    return self.chord_detection.detectChord(c_chroma)
