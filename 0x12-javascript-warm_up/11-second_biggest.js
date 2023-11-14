#!/usr/bin/node
function sec_biggest_int (numbers) {
  const nums = [];
  if (numbers.length <= 3) {
    return (0);
  }
  for (let i = 2; i <= numbers.length - 1; i++) {
    nums[i - 2] = parseInt(numbers[i]);
  }
  nums.sort(function (a, b) {
    return a - b;
  });
  console.log(nums);
  return (nums[nums.length - 2]);
}
console.log(sec_biggest_int(process.argv));
