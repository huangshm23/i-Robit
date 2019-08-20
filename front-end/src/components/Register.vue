<template>
  <div class="register">
    <h1>{{ msg }}</h1>
    <div id="form">
      <label for="mailbox">Mailbox：</label>
      <input type="text" id="mailbox" v-model.trim="mailbox" @blur="jiaoyan1">
      <br>
      <div v-if="!jiaoyanbiaoji1">您的邮箱(注意格式)</div>
      <label for="age">Password：</label>
      <input type="password" id="password" v-model.trim="password" @blur="jiaoyan2">
      <br>
      <div v-if="!jiaoyanbiaoji2">6到8位数字</div>
      <div v-if="status==1">账号已存在</div>
      <div v-if="biaoji == 2" @click="submit" class="buhuanhang">提交</div>
      <div v-else class="buhuanhang">待提交</div>
      <router-link :to="{ path: '/signin' }">转到登录</router-link>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
    jiaoyanbiaoji1:false,
    jiaoyanbiaoji2:false,
    biaoji:0,
    status:-1,
    mailbox:'',
    password:'',
    msg: 'register'
  }
  },
  methods:{
  submit:function(){
  //把mailbox，password发送给后端
  //后端返回状态字
  //0：注册成功，跳转组合推荐页
  //1:账号已存在
  this.postData()
  },
  postData:function(){
  //把mailbox，password发送给后端,并获得返回状态字
  console.log("hello");
  this.$http.post('http://127.0.0.1:8000/users/register/',{params : {account:this.account,password:this.password}}).then(function(res){
      this.status = res.body.status;
      console.log(res.body.status);
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

<style scoped="">
.buhuanhang{
  display:inline
}
</style>
