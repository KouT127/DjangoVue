import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/dist/logger'
import user from './modules/user'

Vue.use(Vuex)

// const debug = process.env.NODE_ENV !== 'production'
// Vue.config.debug = debug

const createStore = () => {
  return new Vuex.Store({
    modules: {
      user: user,
    },
  })
}
export default createStore