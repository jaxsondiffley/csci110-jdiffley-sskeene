import sys
# Resources Used: ChatGPT for questions and explanations
def airtime(heights):
  

    if len(heights) < 3:
        return 0
        # states if the lengh is less then 3 the anwser is 0 
        
    airtime = 0
    for i in range(len(heights) - 2):
        if heights[i+1]-heights[i] > heights[i+2]-heights[i+1]:
            airtime += 1
                
    return airtime

def main():
    # Read all inputs from standard input
    input = sys.stdin.read().split()
   
    # Skip the first element (the total count of elements, e.g., 13)
    heights = [int(x) for x in input[1:]]

    # Call the fruitful function 
    result = airtime(heights)

    #  final answer
    print(result)

if __name__ == '__main__':
    main()




