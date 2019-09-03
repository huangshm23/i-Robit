<template>
  <div class="signin">
    <h1>{{ msg }}</h1>
    <div id="form">
      <label for="mailbox">Mailbox：</label>
      <input type="text" id="mailbox" v-model.trim="mailbox" @blur="jiaoyan1"><br>
      <div v-if="!jiaoyanbiaoji1">您的邮箱（注意格式）</div>
      <label for="age">Password：</label>
      <input type="password" id="password" v-model.trim="password" @blur="jiaoyan2"><br>
      <div v-if="!jiaoyanbiaoji2">6到8位数字</div>
      <div v-if="status==1">账号不存在或密码错误</div>
      <div v-if="status==2">账号未激活</div>
      <div v-if="biaoji == 2" @click="submit" class="buhuanhang">提交</div>
      <div v-else class="buhuanhang">待提交</div>
      <router-link :to="{ path: '/register' }">转到注册</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Signin',
  data () {
    return {
      jiaoyanbiaoji1:false,
      jiaoyanbiaoji2:false,
      biaoji:0,
      status:-1,
      mailbox:'',
      password:'',
      msg: 'signin'
    }
  },
  methods:{
    submit:function(){
      //this.$store.state.is_login=true
      //this.$router.push('/recommendation')
      this.postData();
      //把mailbox，password发送给后端
      //后端返回状态字
      //0：账号密码正确,跳转到组合推荐页
      //1:账号不存在
      //2:账号未激活
    },
    postData:function(){
      //把mailbox，password发送给后端,并获得返回状态字
      this.$http.post('http://178.128.115.175:80/login/',{username:this.mailbox,password:this.password},{emulateJSON:true}).then(function(res){
      this.status = res.body.status;
       console.log(this.status);
      if (this.status == 0) {
        this.$store.state.is_login=true
        this.$router.push('/recommendation')
      }
      },function(err){
      console.log(err);
      });
    },
    jiaoyan1:function(){
      //校验账号
      console.log("jiaoyan1");
      var par1=/^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
      var a=this.jiaoyanbiaoji1;
      this.jiaoyanbiaoji1=par1.test(this.mailbox);
      if(!a && this.jiaoyanbiaoji1)
        this.biaoji++;
      if(this.biaoji>0 && a && !this.jiaoyanbiaoji1)
        this.biaoji--;
      console.log(this.jiaoyanbiaoji1);
    },
    jiaoyan2:function(){
      //校验密码
      console.log("jiaoyan2");
      var par2=/^[0-9]{6,10}$/;
      var a=this.jiaoyanbiaoji2;
      this.jiaoyanbiaoji2=par2.test(this.password);
      if(!a && this.jiaoyanbiaoji2)
        this.biaoji++;
      if(this.biaoji>0 && a && !this.jiaoyanbiaoji2)
        this.biaoji--;
      console.log(this.jiaoyanbiaoji2);
    }
  }
}
</script>

<style scoped>
.buhuanhang{
  display:inline
}
</style>
