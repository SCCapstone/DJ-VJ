"""Test Show Functions"""
import djvj.show as show

SHOW_PARAMS = [None, None, None, None]

# gui.IntroScreen().quit()

# SHOW_PARAMS = [['pitch', 'tempo', 'volume', 'time'],
#                ['<', '>', '=', '='], [500, 120, 20, 5200], ['']]

# initialize show
SHOW = show.Show(SHOW_PARAMS)

# start show
SHOW.start()
