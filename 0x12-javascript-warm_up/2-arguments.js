#!/usr/bin/node
const argument = process.argv.slice(2)
const numArg = argument.length
if (numArg === 0){
  console.log('No Argument')
} else if (numArg === 1){
  console.log("Argument found")
} else {
  console.log("Arguments found")
}
