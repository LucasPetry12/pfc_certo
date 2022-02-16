var criaratividade = document.getElementById('criar-atividade');

criaratividade.addEventListener("click", validarcriaratividade());

function validarcriaratividade() {
    var assunto = document.getElementById('assunto').value;
    var disciplina = document.getElementById('disciplina').value;
    var turma = document.getElementById('turma').value;
    var qtdegrupos = document.getElementById('qtdegrupos').value;
    var autor = document.getElementById('autor').value;
    var pontuacao = document.getElementById('pontuacao').value;

    
    if(assunto == ""){
        document.getElementById('erro-assunto').innerHTML = "Informe o assunto do jogo!"
        return false;
    }else{
        document.getElementById('erro-assunto').innerHTML = "";
    }

    if(disciplina == ""){
        document.getElementById('erro-disciplina').innerHTML = "Informe sua disciplina!"
        return false;
    }else{
        document.getElementById('erro-disciplina').innerHTML = "";
    }

    if(turma == ""){
        document.getElementById('erro-turma').innerHTML = "Informe a turma!"
        return false;
    }else{
        document.getElementById('erro-turma').innerHTML = "";
    }

    if(qtdegrupos == ""){
        document.getElementById('erro-qtdegrupos').innerHTML = "Apenas 2 grupos correspondente!"
        return false;
    }else{
        document.getElementById('erro-qtdegrupos').innerHTML = "";
    }

    if(autor == ""){
        document.getElementById('erro-autor').innerHTML = "Informe o autor!"
        return false;
    }else{
        document.getElementById('erro-autor').innerHTML = "";
    }

    if(pontuacao == ""){
        document.getElementById('erro-pontuacao').innerHTML = "Informe a pontuação da atividade!"
        return false;
    }else{
        document.getElementById('erro-pontuacao').innerHTML = "";
    }
}