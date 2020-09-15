// This is a sample of a thought process pattern for any leetcode problem 

// I want to output the average which uses a total and the total amount of numbers in the array 
// use arr.length to get the total amount of numbers in the array and then divide the total by that.
// to get the total, instantiate var total at the beginning. 
// for each number in the array, we want to add to the total. 
// at the end i want to console.log the average amount.  


function grader(arr){
	var total = 0;
	for (var i =0; i <arr.length; i++){
		total = total + arr[i];
	}
	console.log( total/arr.length); 
}

var avgscores = [90,92,92,90,92,90];
grader(avgscores); 