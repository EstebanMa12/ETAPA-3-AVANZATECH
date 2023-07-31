console.log("Conexión hecha");


const Esteban ={
    name:"Esteban",
    age:23,
    approvedCourse : ["Fundamentos de programación"],
    addCourse(newCourse){
        this.approvedCourse.push(newCourse);
    }
}

/* console.log(Object.keys(Esteban));      
console.log(Object.values(Esteban));
console.log(Object.getOwnPropertyNames(Esteban));
console.log(Object.entries(Esteban)); */


Object.defineProperty(Esteban,"navigator",{
    value: "Brave",
    enumerable: false,
    writable: true,
    configurable: true,
});

Object.defineProperty(Esteban,"pruebaNasa",{
    value: "extraterrestre",
    enumerable: false,
    writable: false,
    configurable: false,
});
Object.defineProperty(Esteban,"Editor",{
    value: "VSCode",
    enumerable: true,
    writable: false,
    configurable: true,
});
Object.defineProperty(Esteban,"terminal",{
    value: "Bash",
    enumerable: true,
    writable: true,
    configurable: false,
});

console.log(Object.getOwnPropertyDescriptors(Esteban));