## Write a Python program which takes a list of single digit integers as input parameter. 
## List may contain values ranging from 1 to 9. The function returns an integer as per logic below: 

* Using the individual elements of the list, find all the possible 3 digits number combinations.
Note: For a single combination, element at same index position should not be considered more than once
Example: Input list: [1, 2, 1] 
Possible three digit combination: 121, 112, 211, 211, 112 and 121. 
Note that 222, 122 and 221 are not considered because in these cases digit 2 occurring at index position 2 is appearing at least twice. In valid combinations listed above, the digit 1 can repeat twice as in the original input list itself the digit 1 is repeated twice. But 111 is not possible combination as 1 is not repeated thrice in the list

* From all the combinations obtained from step 1, consider only the unique combinations.
For the above example: Input list: [1, 2, 1] 
Possible three digit unique combinations obtained from step 1: 121, 112 and 211. 
Note: from the three digit number combinations listed above, duplicates have been removed

* Find the maximum number among the three digit combinations listed above. Append it with the number of three digit combinations obtained in step 2.
For the above example: Input list: [1, 2, 1] 
Possible unique three digit combination obtained from step 2: 121, 112 and 211. 
The maximum number among the above is 211. Append it with the number of three digit combinations. I.e. 3. If you append it to 211, it will become 2113

* Return the generated number in step 3

### Example: 
* Input List: [1, 2, 1, 4]
  Output: 42112
  Possible unique three digit combinations: 121, 124, 112, 114, 142, 141, 211, 214, 241, 412, 411 and 421
  Maximum Number among the combination: 421
  Number of unique combinations: 12
  Hence the output will be 42112.

* Assumptions: 
  Input list would contain at least three elements and maximum of five elements.
  Input list would not contain the digit 0 (zero) 
  Note: No need to validate the assumptions

### Sample Input and Output:
* [1,2,1,4] = 42112
* [2,2,2] = 2221
* [1,3,4,2] = 43224
* [5,2,3,3,2] = 53213
