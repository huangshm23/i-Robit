<template>
  <div id="news">
    <el-backtop :bottom="60"></el-backtop>
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
    <div id=new>
      <div id="new_header">
        {{msg.title}}
      </div>
      <div>
        <div v-html="msg.new_body"></div>
      </div>
      <div id="new_footer">
        <p>日期 : {{msg.datetime}}</P>
        <p>来源 : {{msg.source}}</p>
        <p>链接 : {{msg.source_url}}</p>
      </div>
    </div>
    <el-button-group>
      <el-button type="primary" @click.native="prev" icon="el-icon-arrow-left">上一条</el-button>
      <el-button type="primary" @click.native="next">下一条<i class="el-icon-arrow-right el-icon--right"></i></el-button>
    </el-button-group>
  </div>
</template>

<script>
export default {
  name: 'News',
  data(){
    return{
      activeIndex:'1',
      msg:{
        status:0,
        title:"新闻标题",
        datetime:"2019-10-01",
        source:"中国新闻网",
        source_url:"http://www.baidu.com",
        new_body:"<p>新闻内容</P>"
      }
    }
  },
  methods:{
    logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
      //发送退出请求到后端，返回0成功, 1失败
      this.$http.get(this.$store.state.basicUrl + 'logout/?token=' + this.$store.state.token).then(function(res){
                    if (res.body.status == 1)
                      console.log('退出失败'); 
                },function(){
                    console.log('请求失败处理');
                });
    },
    next:function(){
      this.$http.get(this.$store.state.basicUrl + 'news/?token=' + this.$store.state.token).then(function(res){
                    this.msg.new_body = res.body.news_body;
                    this.msg.datetime = res.body.datetime;
                    this.msg.source_url = res.body.source_url;
                    this.msg.source = res.body.source;
                    this.msg.title = res.body.title;   
                },function(){
                    console.log('请求失败处理');
                });
      //从后端获取新闻，赋值给msg
    },
    prev:function(){
      this.$http.get(this.$store.state.basicUrl + 'news/?token=' + this.$store.state.token).then(function(res){
                    this.msg.new_body = res.body.news_body;
                    this.msg.datetime = res.body.datetime;
                    this.msg.source_url = res.body.source_url;
                    this.msg.source = res.body.source;
                    this.msg.title = res.body.title;   
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
.tag{
  width: 120px;
  font-size: 18px;
}
a{
  text-decoration: none;
}
#new{
  border:5px solid #284EA5;
  width: 80%;
  height:auto;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 10px;
  min-height: 1500px;
  position: relative;
}
#new_header{
  background-color:#BBB;
  font-size: 40px;
  overflow: hidden;
}
#new_footer{
  background-color:#BBB;
  font-size: 24px;
  overflow: hidden;
  position: absolute;
  bottom:0px;
  width: 100%;
}
#new_footer > p{
  text-align: left;
  line-height: 5px;
  margin-left: 30%;
}
.up{
    height: 100vh;
    overflow-y: scroll;
}
</style>
