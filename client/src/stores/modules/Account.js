import getters from '@/stores/getters/Account'
import mutations from '@/stores/mutations/Account'
import actions from '@/stores/actions/Account'

export default {
    namespaced: true,
    getters,
    mutations,
    actions,
    state: {
      // for view
      name: null,
      gender: null,
      birthday: null,
    },
};
