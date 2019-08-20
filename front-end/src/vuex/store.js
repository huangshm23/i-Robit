import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)


const store = new Vuex.Store({
    state : {
        is_login:false,
        result:['A','A','A','A','A','A','A','A','A','A','A','A','A']
    },
    getters:{
        getResult:function(state){
            return state.result
        }
    },
    mutations:{
        update:function(state,n){
            state.result[n.num]=n.value
        }
    }
})

export default store;
