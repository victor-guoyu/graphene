import random


# def random_colors_generator(num_color):
#     colors = []
#     while len(colors) != num_color:
#         random_color = "#" + \
#             ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

#         if random_color not in colors:
#             colors.append(random)

#     return colors

def random_colors_generator():
    random_color_hash = ''.join(
        [random.choice('0123456789ABCDEF') for j in range(6)])
    return f'#{random_color_hash}'
