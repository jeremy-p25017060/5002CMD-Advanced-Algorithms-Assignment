
# Create a class for Person to store personal datas
class Person:
    def __init__(self, name, gender, bio, privacy):
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Bio: {self.bio}")
        print(f"Privacy: {self.privacy}")


# Create a class name for social media (Unweighted Directed Graph)
class SocialMediaGraph:
    def __init__(self):
        # Create a dictionary for class UDGraph
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Check if vertex is added into the list
        if vertex not in self.adj_list:
            # Add new vertex with empty neighbour list to the graph
            self.adj_list[vertex] = []


    def add_edges(self, from_vertex, to_vertex):
        # Check if both vertex is in the list
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            # Add edges together
            self.adj_list[from_vertex].append(to_vertex)
        else:
            raise ValueError ("One or more vertices is not found in the graph!")

    def following_list(self, vertex):
        return self.adj_list.get(vertex, [])

    def followers_list(self, target_vertex):
        followers = [] # List to store followers

        # Loop through all vertices in the graph
        for vertex in self.adj_list:
            # Check if target_vertex is in this vertex's follow list
            if target_vertex in self.adj_list[vertex]:
                followers.append(vertex)  # Add to the list of followers

        return followers

def display_all_users(people):
        print("\n========================")
        print("List of All Users Name:")
        print("========================")
        for key, person in people.items():
            print(f"{key}: {person.name}")

def view_profile(people):
    print("\n========================")
    print("List of All Users Name:")
    print("========================")
    for key, person in people.items():
        print(f"{key}: {person.name}")

    print("=============================")
    user_id = input("Enter user ID to view profile details (1 - 5): ")
    if user_id in people:
        print("\n Selected User Profile:")
        print("=========================")
        people[user_id].display_profile()
    else:
        print("User ID not found!")

def view_following(graph, people):
    print("\n========================")
    print("List of All Users Name:")
    print("========================")
    for key, person in people.items():
        print(f"{key}: {person.name}")

    user_id = input("Enter user ID to view following (1 - 5): ")
    if graph.following_list(user_id):
        print(f"\n{people[user_id].name} is following:")
        for f in graph.following_list(user_id):
            print(f"- {people[f].name}")
    else:
        print("\nUser not found or not following anyone!")

def view_followers(graph, people):
    print("\n========================")
    print("List of All Users Name:")
    print("========================")
    for key, person in people.items():
        print(f"{key}: {person.name}")

    user_id = input("Enter user ID to view followers (1 - 5): ")
    followers = graph.followers_list(user_id)

    if followers:

        print(f"\n{people[user_id].name} is followed by:")
        for f in followers:
            print(f"- {people[f].name}")
    else:
        print("\nNo followers or user not found!")



def main():
    graph = SocialMediaGraph()

    # Create profile for 5 people
    people = {
        "1" : Person("Adam","Male","Photographer","Public"),
        "2" : Person("Brenda","Female","Chef","Private"),
        "3" : Person("Calvin","Male","Singer","Public"),
        "4" : Person("Diva","Female","Model","Public"),
        "5" : Person("Eliot","Male","Student","Private")
    }

    # Add 5 user into the graph
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")

    # Add edges to connect user 1
    graph.add_edges("1","2")
    graph.add_edges("1", "3")
    graph.add_edges("1", "5")


    # Add edges to connect user 2
    graph.add_edges("2", "3")
    graph.add_edges("2", "4")

    # Add edges to connect user 3
    graph.add_edges("3", "4")

    # Add edges to connect user 4
    graph.add_edges("4", "1")
    graph.add_edges("4", "3")

    # Add edges to connect user 5
    graph.add_edges("5", "1")
    graph.add_edges("5", "2")
    graph.add_edges("5", "3")
    graph.add_edges("5", "4")


    while True:
        print("\n===== Welcome to Twitter =====")
        print("1. View All Users Name")
        print("2. View Any User Profile Details")
        print("3. View Any User Following")
        print("4. View Any User Followers")
        print("5. Exit")
        print("==============================")

        choice = input("Select your choice: ")

        if choice == "1":
            display_all_users(people)

        elif choice == "2":
            view_profile(people)

        elif choice == "3":
            view_following(graph, people)

        elif choice == "4":
            view_followers(graph, people)

        elif choice == "5":
            print("\n===== Exiting Twitter =====")
            break

        else:
            print("Please enter input between 1 - 5! Try Again.")


if __name__ == "__main__":
    main()




