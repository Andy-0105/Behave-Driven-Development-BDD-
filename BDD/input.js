
document.getElementById("calculate").addEventListener("submit",function(event){
    event.preventDefault()
    var input = document.getElementById('input_str').value;
    // for (let i=0;i<input.length;i++){
    //     if(!" 12345679+-*/()".includes(input[i])){
    //         return "Invalid Input";
    //     }
    // }
    try{
        document.getElementById("output_str").value=eval(input)
    }
    catch{
        document.getElementById("output_str").value="Invalid Input"

    }
    
})