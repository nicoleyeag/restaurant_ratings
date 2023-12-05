"""Restaurant rating lister."""

#create function
def abc_order_reviews(filename):
#get each line from file
    file = open(filename)

    lines_lst = []

    for lines in file:
        lines = lines.rstrip().split(":")
        lines_lst.append(lines)

        print(f"{lines[0]} is rated at {lines[1]}")


    # print(lines_lst)

        # for line in lines:
        #     print(line)

#store in dictionary abc order
#sorted(lines)
    

# return new dictionary
abc_order_reviews("scores.txt")