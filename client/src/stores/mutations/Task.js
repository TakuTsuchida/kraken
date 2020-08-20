export default {
    setTitle (state, val) {
        state.title = val
    },
    setDescription (state, val) {
        state.description = val
    },
    setDeadline (state, val) {
        state.deadline = val
    },
    setImportance (state, val) {
        state.importance = val
    },
    clearTask (state) {
        state.title = '';
        state.description = '';
        state.deadline = '';
        state.importance = 5;
    },
};
