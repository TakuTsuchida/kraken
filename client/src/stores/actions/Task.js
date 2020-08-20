import axios from 'axios';
import router from '@/router/index'

export default {
    onPost( {state, commit} ) {
        const task = {
            title: state.title,
            description: state.description,
            deadline: state.deadline,
            importance: state.importance,
        };
        axios.post('http://localhost/api/task/new', task)
            .then(res => {
                if (res.status === 201) {
                    commit('clearTask');
                    router.push('/home/task')
                }
            })
            .catch(error => {
                console.error(error);
            })
    },
}
