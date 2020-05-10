import Vue from 'vue';
import App from './App.vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

import router from './router/index';
import store from './stores/index';

const vuetifyOptions = {};
Vue.config.productionTip = false;

Vue.use(Vuetify)
new Vuetify({
  icons: {
    iconfont: 'mdi',
  }
});

new Vue({
  router,
  store,
  render: h => h(App),
  vuetify: new Vuetify(vuetifyOptions),
}).$mount('#app')