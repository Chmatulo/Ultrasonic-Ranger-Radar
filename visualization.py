import pygame
import serial
import math

# Modify Detection Range (units in cm)
detection_range = 15

# Initialize Pygame
pygame.init()

# Set up serial communication with Arduino
arduino = serial.Serial('COM3', 9600)

# Set up the display
width, height = 800, 600
center = (width // 2, height - 100)  # Center of radar at the bottom
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Radar Interface with Persistent Objects')
font = pygame.font.SysFont(None, 24)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIME = (0, 255, 0)
RED = (255, 0, 0)

# Radar settings
radius_step = 50
num_circles = 6
max_radius = radius_step * num_circles
line_width = 2
range_factor = 300 / detection_range

# Create a separate surface for the radar background
radar_background = pygame.Surface((width, height))
radar_background.fill(BLACK)

# Dictionary to store detected objects
# Key is the angle, value is the distance
detected_objects = {}

# Function to draw radar circles and lines on the background surface
def draw_radar_background():
    for i in range(num_circles):
        # Draw radar circles
        pygame.draw.arc(radar_background, GREEN, (center[0] - radius_step * (i+1), center[1] - radius_step * (i+1), radius_step * 2 * (i+1), radius_step * 2 * (i+1)), 0, math.radians(180), 1)

        # add distance text
        range_text = font.render(str(round((i + 1) * (detection_range/num_circles),1)), True, GREEN)
        radar_background.blit(range_text, (center[0] + radius_step * (i+1) - 10, center[1] + 10))
        radar_background.blit(range_text, (center[0] - radius_step * (i+1) - 10, center[1] + 10))

        range_zero = font.render("0", True, GREEN)
        radar_background.blit(range_zero, (center[0] -5, center[1] + 10))

        title = font.render("Ultrasonic Ranger Radar", True, GREEN)
        radar_background.blit(title, (width // 2 - 100, 20))

    # Draw radar lines
    for angle in range(0, 181, 30):
        radians = math.radians(angle)
        x_end = center[0] + max_radius * math.cos(radians)
        y_end = center[1] - max_radius * math.sin(radians)
        pygame.draw.line(radar_background, GREEN, center, (x_end, y_end), line_width)


# Function to draw detected objects from the dictionary
def draw_detected_objects():
    for angle, dist in detected_objects.items():
        if dist > 0:
            draw_object(angle, dist)

# Function to draw a single detected object
def draw_object(angle, dist):
    radians = math.radians(angle)
    xstart = center[0] + dist * range_factor * math.cos(radians)
    ystart = center[1] - dist * range_factor * math.sin(radians)

    xend = center[0] + max_radius * math.cos(radians)
    yend = center[1] - max_radius * math.sin(radians)
    
    # Draw the detected object line
    pygame.draw.line(screen, RED, (xstart, ystart), (xend, yend), line_width)

# Draw the static radar background once
draw_radar_background()

# Function to draw radar sweep line separately
def draw_radar_sweep(angle, previous_angle=None):
    # Erase previous sweep by redrawing the background if previous angle is given
    if previous_angle is not None:
        # Clear the previous sweep line by drawing the background in that area
        radians = math.radians(previous_angle)
        x_end = center[0] + max_radius * math.cos(radians)
        y_end = center[1] - max_radius * math.sin(radians)
        pygame.draw.line(screen, BLACK, center, (x_end, y_end), 3)

        # Redraw the radar background over the cleared line
        screen.blit(radar_background, (0, 0))

        # Redraw all detected objects
        draw_detected_objects()

    # Draw the current sweep line
    radians = math.radians(angle)
    x_end = center[0] + max_radius * math.cos(radians)
    y_end = center[1] - max_radius * math.sin(radians)
    pygame.draw.line(screen, LIME, center, (x_end, y_end), 3)

# Main game loop
running = True
current_angle = 0
previous_angle = None

screen.blit(radar_background, (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for data from Arduino
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        sensor_values = line.split(',')

        if len(sensor_values) == 2:
            angleDeg = int(sensor_values[0])
            dist = float(sensor_values[1])

            if dist <= detection_range:
                draw_object(angleDeg, dist)
            # Update detected objects
                detected_objects[angleDeg] = dist
            else : 
                detected_objects[angleDeg] = 0
            # Draw detected objects

            # Update radar sweep
            draw_radar_sweep(angleDeg, previous_angle)
            previous_angle = angleDeg

    # Update the display
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
