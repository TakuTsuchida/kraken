import getters from '@/stores/getters/Error'
import mutations from '@/stores/mutations/Error'
import actions from '@/stores/actions/Error'

export default {
    namespaced: true,
    getters,
    mutations,
    actions,
    state: {
      // for view
      message: "",
    },
};
