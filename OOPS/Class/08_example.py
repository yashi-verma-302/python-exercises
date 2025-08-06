# Movie Class for Theatre Booking
# Define a Movie class with:
# name, genre, total_seats, booked_seats (default 0)
# Add method:
# book_ticket(count) → increase booked_seats
# available_seats() → returns remaining seats

class Movie:
    def __init__(self, name, genre, total_seats, booked_seats=0):
        self.name = name
        self.genre = genre
        self.total_seats = total_seats
        self.booked_seats = booked_seats

    def book_ticket(self, count):
        if self.booked_seats + count <= self.total_seats:
            self.booked_seats += count
            print(f"{count} ticket(s) booked successfully.")
        else:
            print("Not enough seats available.")

    def available_seats(self):
        return self.total_seats - self.booked_seats

# Test
movie1 = Movie("Inception", "Sci-Fi", 100)

movie1.book_ticket(5)
print("Available seats:", movie1.available_seats())  # Output: 95

movie1.book_ticket(96)
