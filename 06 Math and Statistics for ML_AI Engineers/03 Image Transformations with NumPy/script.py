import numpy as np
import matplotlib.pyplot as plt

# Color code used: 255 = white, 0 = black, 255/2 = gray
heart_img = np.array([[255, 0, 0, 255, 0, 0, 255],
              [0, 255 / 2, 255 / 2, 0, 255 / 2, 255 / 2, 0],
          [0, 255 / 2, 255 / 2, 255 / 2, 255 / 2, 255 / 2, 0],
          [0, 255 / 2, 255 / 2, 255 / 2, 255 / 2, 255 / 2, 0],
              [255, 0, 255 / 2, 255 / 2, 255 / 2, 0, 255],
                  [255, 255, 0, 255 / 2, 0, 255, 255],
                  [255, 255, 255, 0, 255, 255, 255]])

# This is a helper function that makes it easy for you to show images!
def show_image(image, name_identifier):
  plt.imshow(image, cmap="gray")
  plt.title(name_identifier)
  plt.show()

# Show heart image
show_image(heart_img, "Heart Image")
# (6,6) = white
# (3,3) = gray
# (1,3) = black

# Invert color
inverted_heart_img = 255 - heart_img
show_image(inverted_heart_img, "Inverted Heart Image")

# Rotate heart
rotated_heart_img = heart_img.T
show_image(rotated_heart_img, "Rotated Heart Image")

# Random Image
np.random.seed(0)
random_img = np.random.randint(0, 255, (7, 7))
print(random_img)
show_image(random_img, "Random Image")

# Solve for heart image
try:
    x = np.linalg.solve(random_img, heart_img)
except np.linalg.LinAlgError:
    print("random_img is not invertible!")

# Print X matrix
print(x)
show_image(x, "X")

# Recreate heart image
solved_heart_img = random_img @ x
show_image(solved_heart_img, "Solved Heart Image")

