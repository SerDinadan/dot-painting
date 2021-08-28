import colorgram

colors = colorgram.extract('hirst-dot-painting.jpg', 20)
print(colors)
color_list = []

for each_color in range(0, 20):
    color_list_temp = [colors[each_color].rgb.r, colors[each_color].rgb.g, colors[each_color].rgb.b]
    color_list.append(tuple(color_list_temp))

print(color_list)

