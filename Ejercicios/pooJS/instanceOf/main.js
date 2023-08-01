console.log('Conexión echa con main6.js');

function isObject(subject) {
    return typeof subject == "object"
}
function esUnArray(subject) {
    return Array.isArray(subject);
}
//estas 2 funciones son funciones de validacion de datos, estan seran llamads y se les pasaran un parametro, la mayoria de datos se puede validar con typeof, ergo, los arrays son los unicos que tienen un metodo espacial = Array.isArray(objetoAsaberSiEsUnArray)

function deepCopy(subject) {
    let copySubject;
//dentro de sta funcion sucedera todo,el copysubject guardara los datos, este esta esperando a saber si los datos son objetos,arrays u otras cosas como strings
    const subjectIsArray = esUnArray(subject);
    const subjectIsObject = isObject(subject);
//con las constantes subjectIsArray,   subjectIsObject trabajere los datos,  estas son las encargadas de llamar a  las funciones que hicimos fuera de la funcion deepCopy.
  if(subjectIsArray) {
        copySubject = [];
    } else if(subjectIsObject) {
        copySubject = {};
    } else {
        return subject;
    }
    //2da parte del algoritmo
    for(key in subject) {
    //Creamos un bucle for, este bucle (a in b)se puede ejecutar en una estructura de datos como arrays, objetos. Este loop signfica que el elemento a pasara por TODA la estructura de datos de b, y claro, dependieno la posicion de a,este tendra el valor de donde este parado encima. ejemplo: 
    //let array = [52,42,56];
    //for(a in array) {
        //console.log(array[a]);
    //}
            const keyIsObject = isObject(subject[key]);
    //con keyIsObject VUELVO a validar si los datos DENTRO de la estructura de datos YA VALIDADA son objetos o datos. 
    
            if(keyIsObject) {
                copySubject[key] = deepCopy(subject[key]);
    // si resulta que son objetos, entonces iremos copiando y pegando los datos en copySubject, y estos datos se iran copiando de manera identica y exitosa gracias la recursividad deepCopy(subject[key]);
    
    } else {
                if(subjectIsArray) {
                    copySubject.push(subject[key]);
                } else {
                    copySubject[key] = subject[key]
                }
            }
        }
     //estos 2 ultimos casos son mas sencillos ya que simplemente se basa en arrays u elementos que no sean ni arrays ni objetos   
        return copySubject;
    // Y al final de todo, la funcion debe devolver algo,verdad? en este caso, quien es el que almaceno todos los datos de el objeto que copiamos? el copySubject, bien, ese es quien retornamos.
    } 

function requiredParam(param) { // 👈👈
    throw new Error(param + " es obligatorio"); // Este es el mensaje de error generado
    }

function createLearningPath({
    name = requiredParam('name'),
    courses=[]
}) {
    const private ={
        "_name": name,
        "_courses":courses
    };
    const public ={
        get name(){
            return private["_name"]
        },
        set name(newName){
            if(newName.length !=0){
                private["_name"]=newName;
            }else{
                console.warn("Tu nombre debe tener al menos un caracter")
            }
        },
        get courses(){
            return private["_courses"]
        },
    };
    return public
}

function createStudent({
    name = requiredParam('name'),
    email=requiredParam('email'),
    age,
    twitter,
    instagram,
    facebook,
    approvedCourses=[],
    learningPaths=[],
}={}){
    const privateAtributos = {
        "_name": name,
        "_learningPaths":learningPaths,
    };
    const publicAtributos = {
        // El resto de atributos serán públicos:
        email,
        age,
        approvedCourses,
        socialMedia: {
            twitter,
            instagram,
            facebook,
        },
        get name(){
            return privateAtributos["_name"]
        },
        set name(newName){
            if(newName.length !=0){
                privateAtributos["_name"]=newName;
            }else{
                console.warn("Tu nombre debe tener al menos un caracter")
            }
        },
        get learningPaths() { // 👈👈
			return privateAtributos["_learningPaths"];
		},
        set learningPaths(newLP){
            if(!newLP.name){
                console.warn("Tu LP no tiene la propiedad name");
                return
            }
            if (!newLP.courses) {
                console.warn("Tu LP no tiene la propiedad courses");
                return
            }
            if (!esUnArray(newLP.courses)) {
                console.warn("Tu LP no es una lista");
                return
            }
            privateAtributos["_learningPaths"].push(newLP);
        }
        };
        return publicAtributos ;
    }
const Esteban = createStudent({
    name: "Esteban",
    age: 23,
    email: 'daniel@hotmail.com',
});
