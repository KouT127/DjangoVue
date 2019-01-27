

import api from '../../api/user'

//Private
const state = {
  users: [],
  pages: 1
}

//Private
const mutations = {
    setUsers(state, payload) {
      state.users = payload.users
    },
    setPages(state, pages){
      state.pages = pages
    }
}

// Public
const actions = {
  async getUsersAction({ commit, dispatch }, rowPerPage) {
    const endpoint = process.env.API_URL + '/api/users/'
    const payload = {
      users: [],
      rowPerPage: 0
    }
    const response = await api.getUsers('/api/users/').catch((error) => {
      console.log(error)
      return
    })
    payload.users = response.data
    payload.rowPerPage = rowPerPage
    // mutationを触る場合は、commit
    commit('setUsers', payload)
    dispatch('calcPage', payload)
  },
  calcPage({commit}, payload){
    console.log(payload)
    const pages = Math.ceil(payload.users.length / payload.rowPerPage)
    commit('setPages', pages)
  }
}

// Public
const getters = {
  getUsers: (state, getter) => {
    return state.users
  },
  getPages: (state, getter) => {
    return state.pages
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}