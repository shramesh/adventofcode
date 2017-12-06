#input = [0, 2, 7, 0]
input = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
states = []
no_cycles = 0
loop_state = None
while(1):
  #print states

  if loop_state != None:
    loop_no += 1 
    if tuple(input) == loop_state:
      break
    #loop_no += 1
  if loop_state  == None and tuple(input) in states:
    #break
    loop_state = tuple(input)
    loop_no = 0
  states.append(tuple(input))
  no_cycles += 1
  max_num = max(input)
  max_index = input.index(max_num)
  #print max_num,max_index
  input[max_index] = 0
  i = (max_index + 1)%len(input)
  while max_num > 0:
    input[i] += 1
    i = (i + 1)%len(input)
    max_num -= 1
  #print input  
print loop_no
#max_block = max()
