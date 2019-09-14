import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)


const store = new Vuex.Store({
    state : {
        is_login:false,
        result:['A','A','A','A','A','A','A','A','A','A','A','A','A'],
        token:"",
        funds:[{ }],
        rate:0,
        risk_factor:0,
        basicUrl:'http://178.128.115.175:80/',
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
        },
        updateFund:function(state,n){
            for (var x in n) {
                state.funds[x] = n[x];
              }
        },
        updateRate:function(state,n){
            state.rate=n[0]
            state.risk_factor = n[1]
        }
    }
})

export default store;
