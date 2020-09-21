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
                commit('error/setMessage', error, {root: true});
                console.error(error);
            })
    },
    onDelete( {commit}, id) {
        axios.delete(`http://localhost/api/task/delete/${id}`)
            .then(res => {
                if (res.status === 200) {
                    location.reload();
                }
            })
            .catch(error => {
                commit('error/setMessage', error, {root: true});
                console.error(error);
            })
    },
    onGetAll( {commit } ) {
        axios.get('http://localhost/api/task/list')
            .then(res => {
                if (res.status == 200) {
                    commit('setTasks', res.data.tasks);
                }
            })
            .catch(error => {
                commit('error/setMessage', error, {root: true});
                console.error(error);
            })
    },
}
