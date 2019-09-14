import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)


const store = new Vuex.Store({
    state : {
        is_login:false,
        result:['A','A','A','A','A','A','A','A','A','A','A','A','A'],
        token:"",
        combination:{
            recommendation:[
                {
                    name:"中石油",
                    ratio:0.15
                },
                {
                    name:"中石化",
                    ratio:0.6
                },
                {
                    name:"其他",
                    ratio:0.25
                }
            ],
            expected_rate:0.2,
            risk_factor:1.5
        }
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
        risk_factor:0,
        basicUrl:'http://178.128.115.175:80/'
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
