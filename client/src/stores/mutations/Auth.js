export default {
  setUser(state, userData) {
    state.email = userData.email;
    state.password = userData.password;
    state.token = userData.token;
  },
  removeUser(state){
    state.email = null;
    state.password = null;
    state.token = null;
  },
};
