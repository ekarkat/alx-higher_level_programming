#!/usr/bin/node
function factorial (n) {
  let fac = 1;
  for (let i = 1; i < n + 1; i++) {
    if (n === 0) {
      return (1);
    }
    fac = fac * i;
    return (fac);
  }
}
console.log(factorial(parseInt(process.argv[2])));
