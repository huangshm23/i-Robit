<template>
  <div id="exhibition">
    <router-link :to="{ path: '/recommendation' }">组合推荐</router-link>
    <router-link :to="{ path: '/news' }">新闻推荐</router-link>
    <button @click="logout" class="buhuanhang">退出登录</button>
    <hr>
    <h1>Exhibition</h1>
    <div>显示组合</div>
    <div>{{msg}}</div>
    <button @click="simulation">模拟</button>
  </div>
</template>

<script>
export default {
  name: 'Exhibition',
  data(){
    return{
        msg:""
    }
  },
  methods:{
      logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
    },
    simulation:function(){
        //把result发给后端，得到预期收益
        //赋值给msg
    }
  }
}
</script>

<style>
.buhuanhang{
  display:inline
}
</style>