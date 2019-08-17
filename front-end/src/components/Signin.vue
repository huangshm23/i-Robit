<template>
  <div class="signin">
    <h1>{{ msg }}</h1>
    <div id="form">
      <label for="account">Account：</label>
      <input type="text" id="account" v-model.trim="account" @blur="jiaoyan1"><br>
      <div v-if="!jiaoyanbiaoji1">6到8位大小写字母</div>
      <label for="age">Password：</label>
      <input type="password" id="password" v-model.trim="password" @blur="jiaoyan2"><br>
      <div v-if="!jiaoyanbiaoji2">6到8位数字</div>
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
      statue:-1,
      account:'',
      password:'',
      msg: 'signin'
    }
  },
  methods:{
    submit:function(){
      console.log(this.biaoji);
      //把account，password发送给后端
      //后端返回状态字
      //0：账号密码正确,跳转到组合推荐页
      //1:账号不存在
      //2：密码错误
      this.postData();
    },
    postData(){
      //把account，password发送给后端,并获得返回状态字
      this.$http.get('/get.php',{params : {account:this.account,password:this.password}}).then(function(res){
      this.statue = res.body;
      },function(res){
      console.log(res.status);
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
<style scoped>
.buhuanhang{
  display:inline
}
</style>
