import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)


const store = new Vuex.Store({
    state : {
        is_login:false,
        result:['A','A','A','A','A','A','A','A','A','A','A','A','A'],
        token:"",
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
                state.combination.recommendation[x] = n[x];
              }
        },
        updateRate:function(state,n){
            state.combination.expected_rate=n[0]
            state.combination.risk_factor = n[1]
        }
    }
})

export default store;
