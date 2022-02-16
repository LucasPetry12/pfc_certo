import session from "../scripts/auth/session.js";
import references from '../scripts/references/references.js'
import validate from '../scripts/validate/validate.js'
import renderError from '../scripts/renderError/danger.js'
import activityes from '../scripts/api/activityes.js'
import router from './router.js'

(function(){
    
    async function create_activity(data){
       const response = await activityes.create_activity(data)
        localStorage.setItem('code', response.data.code)
        localStorage.setItem('activittye_id', response.data.id)
        router.push('atividade1.html')        
    }

    const authorized  = session.veryfy_session()
    if(authorized === false){
        router.push('index.html')
    }

    const btn_send = references.one('#criar-atividade')
    
    btn_send.addEventListener('click', () => {

        var inputs = references.many_values('#assunto','#disciplina', '#turma', '#qtdegrupos', '#autor', '#pontuacao')
        const can_go = validate.inputs(inputs)

        inputs.series = parseInt(inputs.series.replace(/(\d).+/g,'$1'))
        inputs.qtds_groups = parseInt(inputs.qtds_groups)
        inputs.show_author = parseInt(inputs.show_author)

        if(can_go){
            create_activity(inputs)
        }
        else{
            window.scroll(0,0)
            renderError('Preencha todos os campos!')
        }
    })

})();