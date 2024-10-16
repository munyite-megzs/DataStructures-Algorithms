
/**
 * 
 *  Statement: Given an array, find the second smallest in the array. Print ‘-1’ in the event that it doesn’t exist.

 

Examples

 

Plain Text
Example 1:Input: [1,2,4,7,7,5]Output: Second Smallest : 2

  Second smallest : 2Explanation: The elements are as follows 1,2,3,5,7,7 and hence  second smallest is 2

Example 2:Input: [1]Output: Second Smallest : -1
  Second Largest : -1Explanation: Since there is only one element in the array, it is the smallest element present in the array. There is no second smallest element present.in the arra
 */



function secondSmallest(arr){
    let minimum=Math.min(...arr)
    let minIndex=arr.indexOf(minimum)
    if(arr.length==0||arr.length==1){
        return -1
    }
    else{
       arr.splice(minIndex,1) 
       return Math.min(...arr)
        


    }
}

let array=[1,2,4,7,7,5]
let newArray=secondSmallest(array)
console.log(newArray);