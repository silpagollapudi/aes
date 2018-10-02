[Name]: Saahil Dhulla sd33484
[Name]: Shailen Patel sdp2375 
[Name]: Silpa Gollapudi sg43632
AES README

subBytes
In this method, we used a sBox lookup table that we found from the internet and we replaced the values. We indexed into our array and then replaced it with the value in the sbox. In our debugging process, we had issues with the rows and columns flipping so we flipped our rows and columns for debugging and readability purposes.

shiftRows
We shift each row left n number of times, where n is the 0 indexed row number and went up to a shift of 3 for the fourth row.  After writing out example matrices, we realized that we had to shift all the list elements to the left by a value represented by columns + rows.  If columns + rows is greater than 4, we wrap around by setting the value of the current index to the absolute value of list length minus columns + rows.  We came to this solution by writing out before and after matrices. 

mixColumns
In the mixColumns we used Galois Fields to transform the state on a column-by-column basis. We treated each column as a polynomial and were able to perform the calculation on it, giving us our transformed state matrix.

galoisMultiplication
We were slightly confused on how to matrix multiply with the Galois Fields so we looked up videos on how to do it. We ended up creating a method that allowed us to transform each column by multiplying it by its respective values in the Galois Fields, and it ended up working out for us.

keyExpansion
For 128, we figured out that you you have do n -1 rounds of the previous four methods, subBytes, shiftRows, mixColumns,  and addRoundKey. On the last round however, for 128 bytes we do not have to call mixColumns. We followed the pseudocode that was in the documentation.

rotWord
We take in a word as a parameter and shift each element (byte) to the left by one in place.  We saved a pointer to the first element of our old array in order to set the last element of our new array to that temp value.

subWord
In the same manner as our subBytes method, we substitute every byte of our word parameter with the corresponding value in our S Box list. 

rCon
We take in a word and round number as parameters.  The round number is used to index into our rConTable, which we found online.  Because only the 0th index of the word needs to be changed, we XOR the head of the word list with the element in rConTable at the round number index.  We then return the changed word.

addRoundKey
We XOR the current state matrix with the round key for that particular round and return it.

