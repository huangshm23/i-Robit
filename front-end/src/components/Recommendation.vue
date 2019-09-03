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
      //发送退出请求到后端，返回0成功, 1失败
      this.$http.get('http://178.128.115.175:80/logout/').then(function(res){
                    if (res.body.status)
                      console.log('退出失败'); 
                },function(){
                    console.log('请求失败处理');
                });
    }
  }
}
</script>

<style>
.buhuanhang{
  display:inline
}
</style>