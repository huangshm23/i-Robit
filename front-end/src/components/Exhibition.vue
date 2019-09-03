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
      //发送退出请求到后端，返回0成功, 1失败
      this.$http.get('http://178.128.115.175:80/logout/').then(function(res){
                    if (res.body.status)
                      console.log('退出失败'); 
                },function(){
                    console.log('请求失败处理');
                });
    },
    simulation:function(){
        //把基金种类发送给后端，得到预期收益，赋值给msg
    this.$http.post('http://178.128.115.175:80/simulation/',{
        'fund_ratio': this.$store2.state.funds
    },{emulateJSON:true}).then(function(res){
      msg = "预期收益率： " + res.body.expected_rate;
      },function(err){
      console.log(err);
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