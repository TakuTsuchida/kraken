import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import auth from '@/stores/modules/Auth';
import home from '@/stores/modules/Home';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    home,
  },
  plugins: [createPersistedState({ storage: window.sessionStorage })],
})
