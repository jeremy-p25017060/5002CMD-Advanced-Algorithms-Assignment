import random

def folding_hash(ic, table_size):
    # Convert to string to handle digit-wise operations
    key_str = str(ic)

    # Ensure it is 12 digits
    # key_str.isdigit() to check if the input contains only numbers
    # OR statement if either 1 statement is incorrect
    if len(key_str) != 12 or not key_str.isdigit():
        return None

    # Divide into 3 parts of 4 digits each
    # int to convert string into integer
    # i:i+4 : i = 0 = key_str[0:4]
    # meaning it will split the first 4 digit into a group
    # range(0, 12, 4) means start at 0, stop before 12, steps of 4
    parts = [int(key_str[i:i+4]) for i in range(0, 12, 4)]

    # Sum all the parts
    total = sum(parts)
    return total % table_size


def random12_ic_number():

    # Create random 12 digit number for ic
    # Seperate the ic number into year, month, day
    # The middle 2 digit is the birthplace code, which is the state code of malaysia
    # and the last 4 digit will be the random unique number for every individual in malaysia
    year = random.randint(00,99)
    month = random.randint(1,12)
    day = random.randint(1,28)
    birth_place = random.randint(1, 16)
    unique_num = random.randint(0, 9999)

    # Add up all random digit we get and categorize them
    # by using 02d will get only 2 digit which can start with 0
    born_date = f"{year:02d}{month:02d}{day:02d}"
    bp = f"{birth_place:02d}"
    un = f"{unique_num:04d}"
    ic = born_date + bp + un

    return ic

# Function to insert ic number into hash table
def insert_into_hash_table(ic_list, table_size):
    # Create empty table
    hash_table = [None] * table_size
    # Check how many times collision occurs
    collisions = 0

    # for loop to run each ic number
    for ic in ic_list:
        # Get the index number from folding hash function
        index_num = folding_hash(ic, table_size)
        # Check if the hash table index is taken or not
        # If no then insert as new list
        if hash_table[index_num] is None:
            hash_table[index_num] = [ic]
        else:
            # When collision occurs, append to the list
            hash_table[index_num].append(ic)
            collisions += 1

    return hash_table, collisions

# Functions to create a display table
def display_table(hash_table):
    # Loop to show the index number
    for i, separate_chain in enumerate(hash_table, start = 1):
        if separate_chain:
            print(f"Index[{i}] --> {' -> '.join(separate_chain)}")
        else:
            print(f"Index[{i}]")

def main():
    # Perform 10 rounds of test
    rounds = 10
    table_size = [1009, 2003]
    # Dictionary to store collision counts for each table size
    collision_results = {1009: [], 2003: []}

    # Runs the loop for 10 rounds
    for round_num in range(1, 11):
        # Generate 1000 random ic using function random12_ic_number
        ic_numbers = [random12_ic_number() for _ in range(1000)]

        #
        hash_table_1009, collisions_1009 = insert_into_hash_table(ic_numbers, 1009)
        hash_table_2003, collisions_2003 = insert_into_hash_table(ic_numbers, 2003)

        # Store collision results into the collision list
        collision_results[1009].append(collisions_1009)
        collision_results[2003].append(collisions_2003)

        # Print out the last round of hash table
        if round_num == rounds:
            print("\n\tHash Table Size 1009:")
            print("=============================")
            display_table(hash_table_1009)
            print("\n\tHash Table Size 2003:")
            print("=============================")
            display_table(hash_table_2003)

    # Calculate the average collision value of all 10 rounds
    avg_1009 = sum(collision_results[1009]) / rounds
    avg_2003 = sum(collision_results[2003]) / rounds

    print("\nRound\tCollisions Results: 1009\tCollisions Results: 2003)")
    print("=============================================================")
    for i in range(10):
        # i+1 for loop to make 10 rounds of output
        # :<10 and others is an f-string with width for spacing to replace \t
        print(f"{i + 1:<15}{collision_results[1009][i]:<28}{collision_results[2003][i]}")

    # Print out both table size average collision value
    print("=============================================================")
    print(f"\nAverage Collision Rate for Table Size 1009 = {avg_1009:.2f}")
    print(f"Average Collision Rate for Table Size 2003 = {avg_2003:.2f}")

if __name__ == "__main__":
    main()
