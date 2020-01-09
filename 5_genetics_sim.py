# Determine how likely a child is to have sickle cell anemmia based on a Punnett square

# ask user what each parent's genetic make-up is
# determine likelihood of SCA
# print probability

# big_y is a variable that holds the dominant trait
# small_y is a variable that holds the recessive trait

# Please enter the two genes from Parent 1
parent1 = input ("What is Parent 1's genetic make-up?")
p1_gene1 = parent1[0]
p1_gene2 = parent1[1]


# Please enter the two genes from Parent 2
parent2 = input ("What is Parent 2's genetic make-up?")
p2_gene1 = parent2[0]
p2_gene2 = parent2[1]

# Check for two special cases, otherwise continue below to calculate probability
if p1_gene1 == "Y" and p1_gene2 == "Y":
    if p2_gene1 == "Y" and p2_gene2 == "Y":
        print (0.0)
elif p1_gene1 == "y" and p1_gene2 == "y":
    if p2_gene1 == "y" and p2_gene2 == "y":
        print (100)
else:

    # Check if parent 1's first variable is Y or y
    # Check if parent 1's second variable is Y or y

    if p1_gene1 == "Y":
        p1_gene1 = 0  #nothing is added to p1_gene1
    elif (p1_gene1 == "y"):
        p1_gene1 = 1 #add one to p1_gene1
        
    if p1_gene2 == "Y":
        p1_gene2 = 0  #nothing is added to p1_gene2
    elif (p1_gene2 == "y"):
        p1_gene2 = 1 #add one to p1_gene2

    totalp1_recessive = (p1_gene1 + p1_gene2)




    # Check if parent 2's first variable is Y or y
    # Check if parent 2's second variable is Y or y

    if p2_gene1 == "Y":
        p2_gene1 = 0  #nothing is added to p2_gene1
    elif (p2_gene1 == "y"):
        p2_gene1 = 1  #add one to p2_gene1

    if p2_gene2 == "Y":
        p2_gene2 = 0   #nothing is added to p2_gene2
    elif(p2_gene2 == "y"):
        p2_gene2 = 1  #add one to p2_gene2


    # Sum all of the recessive genes
    totalp2_recessive = (p2_gene1 + p2_gene2)

    # Calculate the probability of SCA based on number of recessive genes
    total_recessive = totalp1_recessive + totalp2_recessive
    probability = ((total_recessive - 1)/4)*100
    print(probability)


