function isMonotonic(nums) {
    let increasing = true;
    let decreasing = true;

    for (let i = 0, j = 1; j < nums.length; i++, j++) {
        if (nums[j] > nums[i]) {
            decreasing = false;
        }
        if (nums[j] < nums[i]) {
            increasing = false;
        }
    }

    return increasing || decreasing;
}

// Example Usage:
console.log(isMonotonic([12,45,67,89])); // true (Monotonic Increasing)
console.log(isMonotonic([60, 50, 46, 42])); // true (Monotonic Decreasing)
console.log(isMonotonic([100, 35, 27, 89]));    // false (Not Monotonic)
