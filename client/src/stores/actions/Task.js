import axios from 'axios';

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
