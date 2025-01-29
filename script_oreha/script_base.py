def craft_item(blue, green, white):
    powder = 0

    req_blue = 33
    req_white = 86
    req_green = 45

    # Calculate initial crafts
    items_crafted = min(blue // req_blue, green // req_green, white // req_white)
    best_crafts = items_crafted

    print(f"Initial craftable items = {best_crafts}")

    # Track trades
    trocas_white = 0
    trocas_green = 0

    while True:
        # Calculate crafts possible with current resources
        crafts_white = white // req_white
        crafts_green = green // req_green

        # Identify the bottleneck (resource with fewer crafts)
        if crafts_white <= crafts_green:
            bottleneck = "white"
            non_bottleneck = "green"
        else:
            bottleneck = "green"
            non_bottleneck = "white"

        improved = False

        # Prioritize trading the non-bottleneck resource
        if non_bottleneck == "green" and green >= 50:
            future_green_crafts = (green - 50) // req_green
            if future_green_crafts >= best_crafts:
                green -= 50
                powder += 80
                trocas_green += 1
                while powder >= 100:
                    powder -= 100
                    blue += 10
                best_crafts = min(blue // req_blue, green // req_green, white // req_white)
                improved = True
            else:
                break
        elif non_bottleneck == "white" and white >= 100:
            future_white_crafts = (white - 100) // req_white
            if future_white_crafts >= best_crafts:
                white -= 100
                powder += 80
                trocas_white += 1
                while powder >= 100:
                    powder -= 100
                    blue += 10
                best_crafts = min(blue // req_blue, green // req_green, white // req_white)
                improved = True
            else:
                break

        # Recalculate crafts possible
        crafts_white = white // req_white
        crafts_green = green // req_green

        # Stop if no further improvement
        if not improved:
            break

    # Craft as many items as possible with the remaining materials
    items_crafted = min(blue // req_blue, green // req_green, white // req_white)
    blue -= items_crafted * req_blue
    green -= items_crafted * req_green
    white -= items_crafted * req_white

    return items_crafted, blue, green, white, trocas_white, trocas_green


# Input: Current materials
blue = int(input("Enter the number of blue materials: "))
green = int(input("Enter the number of green materials: "))
white = int(input("Enter the number of white materials: "))

# Calculate the number of items that can be crafted
items_crafted, remaining_blue, remaining_green, remaining_white, troca_white, troca_green = craft_item(blue, green, white)

# Output the results
print(f"Number of items crafted: {items_crafted}")
print(f"Remaining materials - Blue: {remaining_blue}, Green: {remaining_green}, White: {remaining_white}")
print(f"Traded white {troca_white} times, traded green {troca_green} times")