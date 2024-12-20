def parse_map(input_map):
    """Parse the input map and return a dictionary of antenna frequencies and their positions."""
    antennas = {}
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(antennas, map_width, map_height):
    """Calculate all unique antinodes within the map bounds."""
    antinodes = set()

    for freq, positions in antennas.items():
        # Check each pair of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate the midpoint between the two antennas
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2

                # Calculate the vector between the two antennas
                dx = x2 - x1
                dy = y2 - y1

                # Antinode must be twice the distance from one antenna
                antinode1_x = x1 - dx
                antinode1_y = y1 - dy
                antinode2_x = x2 + dx
                antinode2_y = y2 + dy

                # Add valid antinodes within the bounds of the map
                for antinode_x, antinode_y in [(antinode1_x, antinode1_y), (antinode2_x, antinode2_y)]:
                    if 0 <= antinode_x < map_width and 0 <= antinode_y < map_height:
                        antinodes.add((int(antinode_x), int(antinode_y)))

    return antinodes

def count_unique_antinodes(input_map):
    """Main function to count unique antinodes."""
    antennas = parse_map(input_map)
    map_width = len(input_map[0])
    map_height = len(input_map)
    antinodes = calculate_antinodes(antennas, map_width, map_height)

    # Count unique antinodes
    return len(antinodes)

with open('data/08', 'r') as file:
    lines = file.read().split("\n")

# Count unique antinodes
result = count_unique_antinodes(lines)
print("Number of unique antinode locations:", result)