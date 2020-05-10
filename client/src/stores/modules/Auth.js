import getters from '@/stores/getters/Auth'
import mutations from '@/stores/mutations/Auth'
import actions from '@/stores/actions/Auth'

export default {
    namespaced: true,
    getters,
    mutations,
    actions,
    state: {
      email: '',
      password: '',
      token: '',
    },
};
