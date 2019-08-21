<template>
  <div id="news">
    <router-link :to="{ path: '/recommendation' }">组合推荐</router-link>
    <router-link :to="{ path: '/news' }">新闻推荐</router-link>
    <button @click="logout" class="buhuanhang">退出登录</button>
    <hr>
    <h1>News</h1>
    <div v-html="msg"></div>
    <button @click="submit">下一条</button>
  </div>
</template>

<script>
export default {
  name: 'News',
  data(){
    return{
      msg:"<p>新闻</p>"
    }
  },
  methods:{
    logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
    },
    submit:function(){
      this.$http.get('http://178.128.115.175:80/news/').then(function(res){
                    this.msg = res.body.news_body;   
                },function(){
                    console.log('请求失败处理');
                });
      //从后端获取新闻，赋值给msg
    }
  }
}
</script>

<style>
.buhuanhang{
  display:inline
}
</style>