<template>
  <div id="recommendation">
    <el-menu :default-active="activeIndex" mode="horizontal" background-color="#284EA5" text-color="#fff" active-text-color="#ffd04b">
        <el-menu-item index=1 class="tag">
            <router-link :to="{ path: '/recommendation' }">组合推荐</router-link>
        </el-menu-item>
        <el-menu-item index=2 class="tag">
            <router-link :to="{ path: '/news' }">新闻推荐</router-link>
        </el-menu-item>
        <el-menu-item index=3 class="tag">
            <router-link :to="{ path: '/'}" @click.native="logout">退出账号</router-link>
        </el-menu-item>
    </el-menu>
    <div id="position">
    <el-carousel interval="0" arrow="always" :height="imgHeight">
      <el-carousel-item v-for="item in imgs" :key="item.id">
        <el-row>
          <el-col :span="24"><img ref="imgs" :src="item.idView" class="banner_img"/></el-col>
        </el-row>
      </el-carousel-item>
    </el-carousel>
    <el-button id="button" @click="submit">开始投资</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Recommendation',
  data(){
    return{
      imgs: [
          {id: 0, name:'0', idView: require('../assets/model3.png')},
          {id: 1, name: '1', idView: require('../assets/model2.png')},
          {id: 2, name: '2', idView: require('../assets/model1.png')}
        ],
        imgHeight:'500px'
    }
  },
  methods:{
    logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
      //发送退出请求到后端，返回0成功, 1失败
      this.$http.get('http://129.211.63.182:80/logout/?token=' + this.$store.state.token).then(function(res){
                    if (res.body.status == 1)
                      console.log('退出失败'); 
                },function(){
                    console.log('请求失败处理');
                });
    },
    submit:function(){
      this.$router.push('/questionaire')
    }
  }
}
</script>

<style>
.buhuanhang{
  display:inline
}
.tag{
  width: 120px;
  font-size: 18px;
}
a{
  text-decoration: none;
}
.banner_img{
  height:500px;
  width:400px;
}
#position{
  border:5px solid #284EA5;
  width: 60%;
  min-width: 600px;
  max-width: 800px;
  height:auto;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 10px;
}
#button{
  margin-top: 10px;
  margin-bottom: 50px;
}
</style>