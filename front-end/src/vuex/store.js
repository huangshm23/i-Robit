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

const store2 = new Vuex.Store({
    state : {
        is_login:false,
        funds:[],
        rate:0,
        risk_factor:0
    },
    getters:{
        getResult:function(state){
            return state.funds
        }
    },
    mutations:{
        updateFund:function(state,name,radio){
            state.funds[name]=radio
        },
        updateRate:function(state,rate1,risk){
            state.rate=rate1
            state.risk_factor = risk
        }
    }
})

export default store;
