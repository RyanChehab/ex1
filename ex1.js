let input = prompt("Please enter a positive number: ")

if (!isNaN(input) && input !== "" && input>0){
    console.log("valid number: ",input)
}
else{
    console.log("You didnt enter a valid number")
}

counter=1;
let width = input * 2;


for (let i = 0; i<input;i++){
    console.log('*'.repeat(counter).padStart(width+counter/2))
    counter+=2
}
counter-=4
for (let i= 0; i<input;i++){
    console.log('*'.repeat(counter).padStart(width+counter/2))
    counter-=2
}