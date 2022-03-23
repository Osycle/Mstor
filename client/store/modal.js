// modal.js

export const state = () => ({
  status: false,
  edit_cell: null
})

export const mutations = {
  open(state, cell) {
    state.status = true
    if(cell)
      state.edit_cell = cell
  },
  close(state) {
    state.edit_cell = null
    state.status = false
  },
}
