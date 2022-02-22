"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade
def moon(x,y):
    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)
    # Moon
    arcade.draw_circle_filled(525+x, 525+y, 65, (255, 250, 205))
    # Moon Mouth
    arcade.draw_line(575+x, 505+y, 475+x, 505+y, arcade.color.BLACK, 2)
    # Eyes
    arcade.draw_circle_filled(500+x, 535+y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(547+x, 535+y, 5, arcade.color.BLACK)

def draw_grass():
    # Floor
    arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, (0, 100, 0))
def trees():
    # Another tree, with a trunk and triangle for top
    # Triangle is made of these three points:
    # (400, 400), (370, 320), (430, 320)
    arcade.draw_rectangle_filled(200, 275, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(200,400,125,300,275,300, arcade.csscolor.DARK_GREEN)
def road():
    #Road
    arcade.draw_lrtb_rectangle_filled(0, 600, 200, 100, arcade.csscolor.GREY)
    #Lines of the road
    arcade.draw_lrtb_rectangle_filled(30, 150, 160, 140, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(225, 350, 160, 140, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(420, 580, 160, 140, arcade.csscolor.WHITE)
def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()
    draw_grass()
    moon(0, 0)
    moon(on_draw.moon_x, -5)
    # Add one to the x value, making the moon move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.moon_x += 1
    trees()
    road()
# Create a value that our on_draw.snow_person1_x will start at.
on_draw.moon_x = -435

def main():
    arcade.open_window(600, 600, "Drawing Example")
    arcade.set_background_color((0, 0, 0))
   # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)


    # Keep the window up until someone closes it.
    arcade.run()
main()