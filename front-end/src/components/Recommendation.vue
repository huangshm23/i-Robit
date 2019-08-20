<template>
  <div id="recommendation">
    <router-link :to="{ path: '/recommendation' }">组合推荐</router-link>
    <router-link :to="{ path: '/news' }">新闻推荐</router-link>
    <button @click="logout" class="buhuanhang">退出登录</button>
    <hr>
    <h1>Recommendation</h1>
    <router-link :to="{ path: '/Questionaire' }">开始推荐</router-link>
  </div>
</template>

<script>
export default {
  name: 'Recommendation',
  methods:{
    logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
    }
  }
}
</script>

<style>
.buhuanhang{
  display:inline
}
</style>