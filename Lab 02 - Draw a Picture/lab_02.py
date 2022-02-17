"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((0, 0, 0))

# Get ready to draw
arcade.start_render()
#Floor
arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, (0, 100, 0))
# Moon
arcade.draw_circle_filled(525, 525, 65, (255, 250, 205))
#Moon Mouth
arcade.draw_line(575, 505, 475, 505, arcade.color.BLACK, 2)
#Eyes
arcade.draw_circle_filled(500, 535, 5,arcade.color.BLACK)
arcade.draw_circle_filled(547, 535, 5,arcade.color.BLACK)
# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(200, 275, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(200,400,125,300,275,300, arcade.csscolor.DARK_GREEN)
#Road
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 100, arcade.csscolor.GREY)
#Lines of the road
arcade.draw_lrtb_rectangle_filled(30, 150, 160, 140, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(225, 350, 160, 140, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(420, 580, 160, 140, arcade.csscolor.WHITE)
# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Road to St. Petersburg", 145, 50, arcade.color.WHITE, 20)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
