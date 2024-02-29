
# Invoking the command processor and calling the pause command 
def scrambler(input_data):
    output_data = []
    state = [0, 1, 0, 1, 1, 0, 0]  # Initial state of the scrambler
    for bit in input_data:
        xor_result = bit ^ state[-6] ^ state[-7]  # Calculate the XOR result
        output_data.append(xor_result)  # Append the result to the output
        state.append(xor_result)  # Update the state with the result
        state.pop(0)  # Remove the oldest bit from the state
        print("State:", state)
    return output_data

def descrambler(output_data):
    input_data_result = []
    state = [0, 1, 0, 1, 1, 0, 0]  # Initial state of the descrambler
    for bit in output_data:
        xor_result = bit ^ state[-6] ^ state[-7]  # Calculate the XOR result
        input_data_result.append(xor_result)  # Append the result to the decoded input data
        state.append(bit)  # Update the state with the output bit
        state[-1] = bit  # Update the state based on the calculated value
        state.pop(0)  # Remove the oldest bit from the state
        print("State:", state)
    return input_data_result

# Example usage:
# binary_input = input("Enter binary number: ")  # Input as a string of binary digits
# print('Scrambling: ')
# input_data = [int(bit) for bit in binary_input]  # Convert binary string to a list of integers
input_data = [1,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,0,0]
output_data = scrambler(input_data)  # Scramble the input data
output_data1 = [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
print("\n\n\nDescrambling: ")
# decoded_input_data = descrambler(output_data)  # Descramble the output data
decoded_input_data1 = descrambler(output_data1)  # Descramble the output data
print("\nInput data:           ", input_data)
print("Scrambled output data:", output_data)
# print("\nScrambled output data1:", output_data1)
print("Descrambled input data1:", decoded_input_data1)
# print("Descrambled input data:", decoded_input_data)
print(output_data.count(0))
print(output_data.count(1))
# input()
