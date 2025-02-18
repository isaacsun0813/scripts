# inspired by https://www.youtube.com/watch?v=oAHbLRjF0vo

# Implementation of steffen_boarding method 

def steffen_boarding(empty_plane):
    # Randomly create a list of imaginary passengers with their row and seat
    passengers = []
    for row in range(len(empty_plane)):
        for col in range(len(empty_plane[row])):
            passengers.append((row, col))

    # Divide passengers into window, middle, and aisle groups
    window_seats = [(row, col) for (row, col) in passengers if col in [0, 5]]
    middle_seats = [(row, col) for (row, col) in passengers if col in [1, 4]]
    aisle_seats = [(row, col) for (row, col) in passengers if col in [2, 3]]

    # Step 3: Sort each group back-to-front and alternate odd/even rows
    def steffen_sort(seats):
        back_to_front = sorted(seats, key=lambda x: -x[0])
        odd_rows = [seat for seat in back_to_front if seat[0] % 2 == 1]
        even_rows = [seat for seat in back_to_front if seat[0] % 2 == 0]
        return odd_rows + even_rows

    window_order = steffen_sort(window_seats)
    middle_order = steffen_sort(middle_seats)
    aisle_order = steffen_sort(aisle_seats)

    # Combine our boarding order here
    boarding_order = window_order + middle_order + aisle_order
    return boarding_order

def visualize_boarding(empty_plane, boarding_order):
    plane_visual = [["." for _ in range(6)] for _ in range(25)]

    for idx, (row, col) in enumerate(boarding_order):
        plane_visual[row][col] = "P"
        print(f"Passenger {idx + 1}: Row {row + 1}, Seat {chr(65 + col)}")
        print_plane(plane_visual)
        while True:
            user_input = input("Press 'n' or 'N' and Enter to move to the next passenger: ")
            if user_input.lower() == 'n':
                break
            print("Can always press control + c if u wanna quit (assuming ur on Mac otherwise I don't know what the windows prompt is lol)")
        plane_visual[row][col] = "x"  # Mark the seat as occupied

def print_plane(plane_visual):
    print("\nPlane Layout:")
    for row in plane_visual:
        print(" ".join(row))
    print()

def main():
    """
    Average size of a plane today is 150 passengers. 6 seats per row, 25 rows.
    """
    empty_plane = [[0 for _ in range(6)] for _ in range(25)]
    boarding_order = steffen_boarding(empty_plane)

    print("Steffen Perfect Boarding Order:")
    visualize_boarding(empty_plane, boarding_order)

if __name__ == '__main__':
    main()
