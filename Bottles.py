def print_lyrics():
    for i in range(99, 0, -1):
        print("{0} bottles of beer on the wall, {0} bottles of beer, you take one down, "
              "pass it around! {1} bottle of beer on the wall\n".format(i, i-1))

print_lyrics()