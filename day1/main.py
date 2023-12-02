'''
Advent of Code: Day 1
Completed by Andrew Robinson
2/2 Stars

https://adventofcode.com/2023/day/1

In it's current state, this code only works for part 2. To get it working with part 1, remove references to digit_strings.
'''

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_strings = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}


if __name__ == '__main__':

    # Value to store the sum of our numbers for the calibration value
    sum = 0

    # Open the inputs provided by the website
    with open('cal_doc.txt', 'r') as cal_doc:

        # Iterate over each line
        for line in cal_doc:

            # The first value will always be less than the length of the string
            first_val = '-1'
            first_index = len(line) - 1

            # The last value will be no smaller than 0
            last_val = '-1'
            last_index = 0

            # Iterate over all possible values, 0-9 + One-Nine
            # to find the first-most value
            for value in digits + list(digit_strings.keys()):

                index = line.find(value)

                # If the index is smaller then the current front-most value,
                # repalce it. Ignore if the value is -1 as this is what's returned
                # if there is nothing found
                if index < first_index and index != -1:
                    first_index = index
                    first_val = value

            for value in digits + list(digit_strings.keys()):

                # The rfind is important here and kicked my butt for too long.
                index = line.rfind(value)

                # If the index is larger then the current last-most value,
                # repalce it. Ignore if the value is -1 as this is what's returned
                # if there is nothing found
                if index >= last_index and index != -1:
                    last_index = index
                    last_val = value

            # Map the string values back to single digits
            if first_val in digit_strings:
                first_val = digit_strings[first_val]

            # Map the string values back to single digits
            if last_val in digit_strings:
                last_val = digit_strings[last_val]

            # Debug statement to check outputs
            #print(line.replace('\n',''), first_index, first_val, last_index, last_val)

            # Generate the integer to be added to ths um
            int_value = int(first_val + last_val)

            # Add the current integer value to the sum
            sum += int_value

        # Display the output
        print(sum)
