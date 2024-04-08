def print_color(text, color):
    print("\033[{}m{}\033[0m".format(color, text), end='')

alphabet = []
colors = ["31", "32", "33", "34", "35", "36", "37", "91", "92", "93", "94", "95", "96", "97"]
color_index = 0

for letter in range(ord('a'), ord('z')+1):
    alphabet.append(chr(letter))
    print_color(chr(letter), colors[color_index])
    color_index = (color_index + 1) % len(colors)

print("\nAlphabet:", alphabet)
