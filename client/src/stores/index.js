import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import auth from '@/stores/modules/Auth';
import account from '@/stores/modules/Account';
import task from '@/stores/modules/Task';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    account,
    task,
  },
  plugins: [createPersistedState({ storage: window.sessionStorage })],
})
