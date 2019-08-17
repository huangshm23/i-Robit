<template>
  <div class="register">
    <h1>{{ msg }}</h1>
    <div id="form" v-for="q in questions" :key="q.num">
      <div>{{q.num}}:{{q.question}}</div>
      <div v-for="o in q.options" :key="o.op">
          <input v-if="o.op=='a'" type="radio" :name="q.num" :value="o.op" checked=true>
          <input v-else type="radio" :name="q.num" :value="o.op">
          {{o.option}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
  return {
  biaoji:0,
  msg: 'Questionaire',
  questions:[
      {
        num:1,
        question:"1?",
        options:[
            {op:"a",option:"a"},
            {op:"b",option:"b"}
        ]
      },
      {
        num:2,
        question:"2?",
        options:[
          {op:"a",option:"a"},
          {op:"b",option:"b"},
          {op:"c",option:"c"}
        ]
      }
  ]
  }
  },
  methods:{
    submit:function(){
    console.log("click");

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="">
.buhuanhang{
  display:inline
}
</style>