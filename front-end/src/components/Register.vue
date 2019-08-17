<template>
  <div class="register">
    <h1>{{ msg }}</h1>
    <div id="form">
      <label for="account">Account：</label>
      <input type="text" id="account" v-model.trim="account" @blur="jiaoyan1">
        <br>
          <div v-if="!jiaoyanbiaoji1">6到8位大小写字母</div>
          <label for="age">Password：</label>
          <input type="password" id="password" v-model.trim="password" @blur="jiaoyan2">
            <br>
              <div v-if="!jiaoyanbiaoji2">6到8位数字</div>
              <router-link :to="{ path: '/signin' }">登录</router-link>
              <br>
                <div v-if="biaoji == 2">提交</div>
                <div v-else>待提交</div>
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
  statue:-1,
  account:'',
  password:'',
  msg: 'register'
  }
  },
  methods:{
  submit:function(){
  console.log(this.biaoji);
  //把account，password发送给后端
  //后端返回状态字
  //0：注册成功，跳转个人主页
  //1:账号已存在
  this.postData()
  },
  postData(){
  //把account，password发送给后端,并获得返回状态字
  console.log("hello");
  this.$http.get('/get.php',{params : {account:this.account,password:this.password}}).then(function(res){
  this.statue = res.body;
  },function(err){
  console.log(err);
  });
  },
  jiaoyan1:function(){
  //校验账号
  console.log("jiaoyan1");
  var par1=/^[a-zA-Z]{6,10}$/;
  var a=this.jiaoyanbiaoji1;
  this.jiaoyanbiaoji1=par1.test(this.account);
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="">

</style>
