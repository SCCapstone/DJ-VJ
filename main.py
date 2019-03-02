""" main run file for the project"""
import djvj.gui as gui
import djvj.show as show

# initialize GUI
# gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
# print("This will be passed to the audio listener: %s" % gui.audio_attr)
#
# print("This will be passed to the video instance: %s" % gui.video_attr)

# get show params from gui: [[params], [rules], [values], [videos]]
# SHOW_PARAMS = [gui.show[0],
#                gui.show[1], gui.show[2], gui.show[3]]

print(gui.moments)
# this is only for testing purposes, show that the file path stays the same

# SHOW_PARAMS = [['pitch', 'tempo', 'volume', 'time'],
#                ['<', '>', '=', '='], [500, 120, 20, 5200], ['']]

# SHOW_PARAMS = [['pitch', 'pitch'],
#                ['<', '>'], [500, 500], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['tempo', 'tempo'],
#                ['<', '>'], [120, 120], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

SHOW_PARAMS = [['time', 'time'],
               ['<', '>'], [10, 10], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['pitch', 'time', 'pitch', 'time', 'pitch', 'time', 'pitch', 'time'],
#                ['<', '<', '>', '<', '<', '>', '>', '>'], [500, 30, 500, 30, 500, 30, 500, 30], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV"]]

# initialize show
#SHOW = show.Show(SHOW_PARAMS)

# start show
#SHOW.start()
