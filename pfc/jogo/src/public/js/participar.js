var participar = document.getElementById("participar");

participar.addEventListener("click", validarparticipar);

function validarparticipar(){
    
    var nome = document.getElementById('nome-aluno').value;
    var codigo = document.getElementById('codigo-atividade').value;

    if(nome == ""){
        document.getElementById('erro-nome-aluno').innerHTML = "Isira seu nome completo!"
        return false;
    }else{
        document.getElementById('erro-nome-aluno').innerHTML = "";
    }

    if(codigo == ""){
        document.getElementById('erro-codigo-atividade').innerHTML = "Isira o código da atividade!"
        return false;
    }else{
        document.getElementById('erro-codigo-atividade').innerHTML = "";
    }
}