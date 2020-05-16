import axios from 'axios';
import router from '@/router/index'

export default {
  signIn({commit}, credential) {
    // TODO http://localhost/api は共通化するべきである。
    axios.post('http://localhost/api/auth/signIn', credential)
      .then(res => {
        if (res.status === 200 && 'token' in res.data) {
          const userData = {
            email: credential.email,
            password: credential.password,
            token: res.data.token,
          }
          commit('setUser', userData);
          router.push('/home')
        }
      })
      .catch(error => {
        console.error(error);
      })
  },
  signUp({commit}, credential) {
    // TODO http://localhost/api は共通化するべきである。
    axios.post('http://localhost/api/auth/signUp', credential)
      .catch(error => {
        console.error(error);
      })
    commit('removeUser');
    router.push('/auth/signIn');
  },
}
