#!/usr/bin/node

exports.esrever = function (list) {
	let rev = [];
	let li = list;
	const l = list.length
	for (let i = 0; i < l; i++) {
		rev.push(li.pop());
	}
	return (rev);
}
