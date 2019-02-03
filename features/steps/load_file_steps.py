"""
 Behavior test for the overall functionality of the program
 These steps define the features present in load_file.feature
"""
import threading
import behave
import djvj.djvj_GUI as gui
import djvj.pitch as audio_listener
import djvj.Visual as video

@given('program is loaded with a file arguement')
def step_impl(context):
    """ initialize gui and get parameters for audio and video """
    gui.init()
    print("This will be passed to the audio listener: %s" % gui.audio_attr)
    print("This will be passed to the video instance: %s" % gui.video_attr)

@when('audio and video are initialized')
def step_impl(context):
    """ initialize audio and video """
    context.VISUAL = video.Visual(gui.video_attr)
    AUDIO_LISTENER = audio_listener.AudioListener(
        gui.audio_attr, "live", context.VISUAL)

    lock = threading.RLock()
    analyze_pitch_thread = threading.Thread(
        target=AUDIO_LISTENER.pitch_detection.analyze_pitch, args=(AUDIO_LISTENER.VISUAL, lock,))
    analyze_pitch_thread.start()

@then('the proper video would be played with correct parameters')
def step_impl(context):
    """
    'play' the video, in this case just confirm that the video would be played
    if the program was launched properly
    """
    context.VISUAL.validate()
