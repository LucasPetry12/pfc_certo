import router from './router.js'
(() =>{
  async  function get_my_activityes(){
       const response = await axios.get('http://localhost:5000/activity/get',{headers:{"Authorization":'Bearer '+ localStorage.getItem('token')}})
    if(response.data){
        if(response.data.length > 0){
            response.data.forEach(el => {
                var li = document.createElement('li')
                var a = document.createElement('a')
                var span = document.createElement('span')
                a.href = 'atividade1.html'
                a.addEventListener('click', (e) => {
                    e.preventDefault()
                    localStorage.setItem('code', el.code)
                    router.push('atividade1.html')
                })
                a.innerHTML = el.code.replace(/'/g,'')
                li.appendChild(a)
                li.appendChild(span)
                document.querySelector('.activityes').appendChild(li)
            })
        } 
    } 
    }
    get_my_activityes()
})()
