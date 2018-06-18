# Layout
size(1024, 1024)

# Fonts
font("fonts/WoodbineGX.ttf")
fontSize(140)

# Set axis from font
for axis, data in listFontVariations().items():
    print((axis, data))

# Variables using vanilla ui widgets.
Variable([
    dict(name="input_text", ui="EditText", args=dict(text='LANGUAGE')),
    dict(name="slider", ui="Slider", args=dict(value=100, minValue=100, maxValue=200)),
], globals())

# console output, uncomment for additional info
print("Slider-:",int(slider))
print("Text---:",input_text)

# Set grid variables
canvas     = 1024  # size of the gif in pixels
margin     = 64  # distance from edge of canvas

def grid():
    # draw the grid
    fill(None)
    # stroke(0.75)
    stroke(1, 0.4, 0.3,)
    strokeWidth(1)
  
    # grid X-axis
    stepx  = -64  # step in sequence on x axis             
    incx   =  64  # grid increment
    for x in range(15):
        save()
        stepx = stepx + incx
        polygon((margin + stepx, margin), (margin+stepx, canvas-margin))
        restore()

    # grid Y-axis
    stepy  = -64  # step in sequence on y axis 
    incy   =  64  # grid increment
    for y in range(15):
        save()
        stepy = stepy + incy
        polygon((margin, margin + stepy), (canvas-margin, margin+stepy))
        restore()

def main():
    # Uncomment to draw grid
    grid()
    # Set text fill
    fill(0)
    strokeWidth(2)
    stroke(None)
    tracking(None)
    for i in range(1,6):
        # Magic 
        fontVariations(wght=(slider-(i*32)))
        # Draw text
        text(input_text, 205, (832-(i*128)))


if __name__ == "__main__":  
    main()
