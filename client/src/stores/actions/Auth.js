import axios from 'axios';
import router from '@/router/index'

export default {
  login({commit}, credential) {
    // TODO http://localhost/api は共通化するべきである。
    axios.post('http://localhost/api/login', credential)
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
  },
  signUp({commit}, credential) {
    // TODO http://localhost/api は共通化するべきである。
    axios.post('http://localhost/api/auth/signUp', credential)
      .then(res => {
        // TODO resをどうするか？
        console.log(res);
        commit('removeUser');
        router.push('/auth/signIn')
      })
      .catch(error => {
        console.error(error);
      })
  },
}
