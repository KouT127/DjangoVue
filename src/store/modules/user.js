
import axios from 'axios'

//Private
const state = {
  users: []
}

//Private
const mutations = {
    getUsers(state, payload) {
        state.desserts = payload.users
    },
}

// Public
const actions = {
  async getUsersAction({ commit, state, dispatch }, rowPerPage) {
    const endpoint = 'http://localhost:8000/api/users'
    const payload = {
      users: [],
    }
    const response = await axios.get(endpoint)
    .catch(err => {
     return Promise.reject(err.response)
    })
    if (response.status !== 200) {
      let error = error({
        statusCode: response.status,
        message: response.data.message,
      })
      return Promise.reject(error)
    }
    console.log(response)
    payload.users = response.data.users
    // mutationを触る場合は、commit
    commit('getUsers', payload)
    return Promise.resolve()
  }
}

// Public
const getters = {
  getUsers: (state, getter) => {
    return state.users
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}