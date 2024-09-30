# Programmer: Teresa Fischer
# Date: 9/30/24
# Title: Program #1: Kilometer Converter

# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
    kilometers = int(input('Enter a distance in kilometers:'))
    miles = kilometers * 0.6214
    ######################    


    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion
    result = kilometer_conversion('number')

    # Display the miles
    print('That is', result, 'miles!')
