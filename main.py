#Define a function to distinguish between uppercase and lowercase
def character_case(character):
    if character==character.upper():
        #if character in a line is an Uppercase then it will return a string called 'upper' and if not then 'lower'
        return 'upper'
    else:
        return 'lower'

#define a function that will determine how many letters in a line
def process_string(line):
    #we will use the len function to determine the length of how many lower case characters in one line
    #Inside the list, we will use list comprehension for the loop to filter out which character in the line is categorized as 'lower' and 'upper'
    #and store it in the list
    #To decode this into human readable, for every value of x in every line => if character_case function is either 'upper' or 'lower' => put it in the list
    lower_case = len([x for x in line if character_case(x)=='lower'])
    upper_case = len([x for x in line if character_case(x)=='upper'])
    #We need to filter out which one is special character so we doing something similar to the 2 lines above
    #using isalnum, apply the same logic above, if the character of a line is not a number or an alphabet letter then it will return false
    #And it will append the special character into the list
    special_character = len([x for x in line if x.isalnum()==False])
    #Same thing but will append any numbers into the list
    nums = len([x for x in line if x.isnumeric()])
    #The below line of code is our complexity requirement which is more than 14 characters, 1 lower and upper, 2 special ,and 2 numbers
    if len(line)>14 and lower_case>=1 and upper_case>=1 and special_character>=2 and nums>=2:
        return True
    else:
        return False

#Function that write the output file
def write_to_output_file(string,filename):
    #open the file with write permission
    file = open(filename,'w')
    #write the file
    file.write(string)
    #close the file
    file.close()

def main():
    #Encoding is UTF8 since we are also reading special character
    data = open('password.txt','r',encoding="utf8").readlines()
    #count for strong and weak passphrase
    strong_passphrase = 0
    weak_passphrase = 0
    for line in data:
        if process_string(line):
            strong_passphrase+=1
        else:
            weak_passphrase+=1
    print(f'Strong passphrase count: {strong_passphrase}')
    print(f'Weak passphrase count: {weak_passphrase}')
    write_to_output_file(f'Strong  passphrase count: {strong_passphrase}'+'\n'+ f'Weak passphrase count: {weak_passphrase}', 'Output.txt')

main()
