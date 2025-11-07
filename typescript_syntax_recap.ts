//  Hashmap
const seen: Map<string, number> = new Map()

//  Hashset
const nums: Set<number> = new Set()

//  Array methods
const arr: number[] = [1, 2, 3, 4, 5]

//  Initialize 2D array
const two_D_array = Array.from({ length: 5 }, () =>
	Array.from({ length: 3 }, (_, i) => i)
)

// fill with 0s
arr.fill(0)

const arr2 = arr.slice(1, 3)

const arr3 = [...arr]

const arr4 = arr.concat(arr2)

//  Check if all entries match predicate
const allGreaterThanZero = arr.every((num) => num > 0)

const evenNumbers = arr.filter((num) => num % 2 == 0)

const squaredArray = arr.map((num) => num * num)

const greaterThanTen = arr.find((num) => num > 10)
const indexGreaterThanTen = arr.findIndex((num) => num > 10)

const includesFive = arr.includes(5)
const indexofFive = arr.indexOf(5)

const joinedStringe = arr.join('-')
