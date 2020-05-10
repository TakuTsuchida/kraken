export default {
  initMenuListFlg(state) {
    state.menuListFlg = false;
  },
  openMenuList(state) {
    console.log('check open');
    state.menuListFlg = false;
    state.menuListFlg = true;
  },
};
