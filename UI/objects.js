var Animal = {
    type: "Invertibrates",
    dispayType: function () { alert("type is :" + this.type) }
};// JavaScript source code

var Horse = Object.create(Animal)

var Trainer = {
    name: "ABC",
    subjects: ["Math", "Physics", "Chem"],
    teaches :["F", "S",],
    age: 60
}
var properties="";
for (p in Trainer) { properties += p + ":" }
console.log(properties)