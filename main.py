""" main run file for the project"""
# import djvj.gui as gui
import djvj.gui_moments as gui
import djvj.moment as moment
import djvj.show as show

# initialize GUI
gui.init()
# print(gui.moments)
MOMENTS = moment.create_moments(gui.moments)

# gui_moments_list = [[['pitch', '<', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV'], ['time', '<', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV']], [['pitch', '>', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4'], ['time', '<', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4']],
#                     [['pitch', '<', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4'], ['time', '>', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4']], [['pitch', '>', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV'], ['time', '>', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV']], []]
#
# MOMENTS = moment.create_moments(gui_moments_list)


# initialize show
SHOW = show.Show(MOMENTS)

# start show
SHOW.start()
