function EnviarContacto(){
    var genero="";
    var a=document.getElementById("nom").value;
    var b=document.getElementById("correo").value;
    var c=document.getElementById("fono").value;
    var d=document.getElementById("fecha").value;
    var e=document.getElementById("edad").value;
    var f=parseInt(document.getElementById("genero").value);

        if (f===1){
            genero='Mujer';
        }
        if (f===2){
            genero='Hombre';
        }
        if (f===3){
            genero='Otro Genero';
        }


    var mensaje = "Contacto Hespérides: \n"
                   +"Nombre: " + a + "\n" + "Correo: " + b + "\n" +
                    "Teléfono: " + c + "\n" + "Fecha: " + d + "\n" + 
                    "Edad: " + e + "\n" + "Genero: " + genero;
                   
    document.getElementById("textocontacto").value=mensaje;
}
//VALIDA FORMULARIO CONTACTO
/*$(function(){
    $("#contact-form").validate({
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            fono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
            edad:{
                required:true,
                number:true
            },
            genero:{
                required:true
            }

        },//rules
        messages:{
            nom:{
                required: 'Ingrese su nombre',
                minlength: 'Caracteres insuficientes(5)'
            },
            correo:{
                required: 'Ingrese correo de contacto',
                email: 'Formato de correo inválido'
            },
            fono:{
                required: 'Ingrese teléfono',
                minlength: 'Cantidad de dígitos insuficientes(9)'
            },
            fecha:{
                required: 'Seleccione una fecha válida',
                min: 'Fecha no corresponde'
            },
            edad:{
                required: 'Ingrese su edad',
                min: 'Ingrese una edad mayor (10 o más)',
                max: 'Edad no existe' 
            },
            genero:{
                required: 'Seleccione un género'
            },
        },//MESSAGES
    })//VALIDATE
})//FUNCION*/

//CALCULADORA IMC

$(document).ready(function(){
    $("#calcular").click(function(){
        var a= parseInt($("#peso").val());
        var b= parseInt($("#altura").val());
        var res=(Math.round(a/((b*b)/10000)));
        $("#resultado").val(res);
    })
});