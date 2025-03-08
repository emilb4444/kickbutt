import sys

def calculate_kicktobutt():
    user_name = input("Who r u?\n")
    person_to_get_kicked = input("Who needs to be kicked in butt?\n")
    unskibidiness = input("How unskibidi are they on a scale of 1 to 10?\n")
    unskibidiness = int(unskibidiness)
    if unskibidiness < 1 or unskibidiness > 10:
        print("gurl try that in bounds\n")
        calculate_kicktobutt()
        sys.exit()
    sigma = int(input("How much more sigma are you than " + person_to_get_kicked + " because they are unskibidi on a scale from 1 to 10?\n"))
    if sigma < 1 or sigma > 10:
        print("gurl try againnnn play fair\n")
        calculate_kicktobutt()
        sys.exit()
    kicks_in_butt = (unskibidiness * 3) + (sigma * 5)
    stiletto_heels = False
    if sigma > 5 or unskibidiness > 5 :
        stiletto_heels = True
    stmt = person_to_get_kicked + " is sentenced to " + str(kicks_in_butt) + " kicks in butt"
    if stiletto_heels is True:
        stmt =stmt + ", with the excecutioner wearing stiletto heels..."
    print(stmt)


if __name__ == '__main__':
    calculate_kicktobutt()