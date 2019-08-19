import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
    is_login:false
}

export default new Vuex.Store({
    state
})