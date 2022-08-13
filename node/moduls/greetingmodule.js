/**создание модуля greeting */
console.log("greeting module");
module.exports.date = currentDate;
module.exports.getMessage = function(name){
    let hour = currentDate.getHours();
    if(hour > 16)
    return "good evening, " + name;
    else if(hour > 10)
    return "good day, " + name;
    else
    return "good morning, " +name;
}