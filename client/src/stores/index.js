import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import auth from '@/stores/modules/Auth';
import account from '@/stores/modules/Account';
import task from '@/stores/modules/Task';
import error from '@/stores/modules/Error';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    account,
    task,
    error,
  },
  plugins: [createPersistedState({ storage: window.sessionStorage })],
})
