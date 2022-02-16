var headers = {
    'Authorization': 'Bearer '+localStorage.getItem('token'),
    'Content-Type': "application/json"
}
const api = {
    async create_activity(data){
        const response = axios.post('http://localhost:5000/activity/create',data, {headers} )
        return response
    }
}
export default api