function validate(str) {
    if(str.match(/^\w{2,10}@.+$/i)){
        document.getElementById('button').disabled = false;
        alert("Funciona")
    }
    console.log(str);
}