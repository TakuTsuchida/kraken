import getters from '@/stores/getters/Task'
import mutations from '@/stores/mutations/Task'
import actions from '@/stores/actions/Task'

export default {
    namespaced: true,
    getters,
    mutations,
    actions,
    state: {
      // for view
      title: '',
      description: '',
      deadline: '',
      importance: 5,
      tasks: [],
    },
};
