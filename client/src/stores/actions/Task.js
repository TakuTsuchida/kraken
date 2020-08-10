import axios from 'axios';
import router from '@/router/index'

export default {
    onPost(task) {
        console.log(task);
        axios.post('http://localhost/api/task/new', task)
            .then(res => {
                if (res.status === 201) {
                    router.push('/home/task')
                }
            })
            .catch(error => {
                console.error(error);
            })
    },
}
