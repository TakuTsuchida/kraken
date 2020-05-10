import getters from '@/stores/getters/Home'
import mutations from '@/stores/mutations/Home'
import actions from '@/stores/actions/Home'

export default {
    namespaced: true,
    getters,
    mutations,
    actions,
    state: {
      // for view
      menuListFlg: null,
    },
};
