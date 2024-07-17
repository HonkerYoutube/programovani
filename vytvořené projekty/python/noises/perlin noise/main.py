import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from noise import pnoise2

# Step 1: Generate a single layer of Perlin noise
def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity):
    noise = np.zeros((height, width))  # Create an empty array for noise
    
    for y in range(height):
        for x in range(width):
            noise[y][x] = pnoise2(
                x / scale,
                y / scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=width,
                repeaty=height,
                base=0
            )
    return noise

# Step 2: Blend multiple layers of Perlin noise
def blend_perlin_noises(width, height, scales, octaves, persistences, lacunarities):
    blended_noise = np.zeros((height, width))  # Create an empty array for blended noise
    
    for scale, octave, persistence, lacunarity in zip(scales, octaves, persistences, lacunarities):
        blended_noise += generate_perlin_noise(width, height, scale, octave, persistence, lacunarity)
    
    # Normalize the noise to be between 0 and 1 for display
    min_val, max_val = np.min(blended_noise), np.max(blended_noise)
    blended_noise = (blended_noise - min_val) / (max_val - min_val)
    
    return blended_noise

# Step 3: Set parameters for blending
width, height = 500, 500  # Size of the noise pattern

# Initial slider values
init_scales = [50, 100, 200]
init_octaves = [1, 2, 4]
init_persistences = [0.5, 0.5, 0.5]
init_lacunarities = [2.0, 2.0, 2.0]

# Create the initial noise pattern
blended_noise = blend_perlin_noises(width, height, init_scales, init_octaves, init_persistences, init_lacunarities)

# Step 4: Display the blended noise
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.5)
img = ax.imshow(blended_noise, cmap='gray')
plt.colorbar(img)

# Create sliders for scales, octaves, persistences, and lacunarities
axcolor = 'lightgoldenrodyellow'

# Define slider positions and labels
slider_positions = [
    (0.1, 0.4, 0.65, 0.03),
    (0.1, 0.35, 0.65, 0.03),
    (0.1, 0.3, 0.65, 0.03),
    (0.1, 0.25, 0.65, 0.03),
]

slider_labels = ['Scale', 'Octave', 'Persistence', 'Lacunarity']
sliders = []

# Create and add sliders
for i in range(3):
    scale_slider = Slider(plt.axes(slider_positions[0], facecolor=axcolor), f'Scale {i+1}', 1, 300, valinit=init_scales[i])
    octave_slider = Slider(plt.axes(slider_positions[1], facecolor=axcolor), f'Octave {i+1}', 1, 5, valinit=init_octaves[i])
    persistence_slider = Slider(plt.axes(slider_positions[2], facecolor=axcolor), f'Persistence {i+1}', 0.1, 1.0, valinit=init_persistences[i])
    lacunarity_slider = Slider(plt.axes(slider_positions[3], facecolor=axcolor), f'Lacunarity {i+1}', 1.0, 4.0, valinit=init_lacunarities[i])

    sliders.append((scale_slider, octave_slider, persistence_slider, lacunarity_slider))

    slider_positions = [(pos[0], pos[1] - 0.05, pos[2], pos[3]) for pos in slider_positions]

def update(val):
    scales = [sliders[i][0].val for i in range(3)]
    octaves = [sliders[i][1].val for i in range(3)]
    persistences = [sliders[i][2].val for i in range(3)]
    lacunarities = [sliders[i][3].val for i in range(3)]
    
    new_noise = blend_perlin_noises(width, height, scales, octaves, persistences, lacunarities)
    img.set_data(new_noise)
    fig.canvas.draw_idle()

for slider_set in sliders:
    for s in slider_set:
        s.on_changed(update)

plt.show()
