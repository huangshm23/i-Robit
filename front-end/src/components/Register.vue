<template>
  <div class="signin">
    <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box" id="denglukuan">
      <h3 class="login-title">注册账户</h3>
      <el-form-item label="账号" prop="mailbox">
        <el-tooltip class="item" effect="dark" content="正确格式: 1...2@qq.com" placement="right">
          <el-input type="text" placeholder="请输入账号" v-model="form.mailbox"/>
        </el-tooltip>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-tooltip class="item" effect="dark" content="正确格式: 6位数字" placement="right">
          <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
        </el-tooltip>
      </el-form-item>
      <el-form-item>
        <el-button v-if="biaoji==2" type="success" @click.native="submit" class="zuceanniu">注册</el-button>
        <el-button v-else type="info" @click.native="false_submit" class="zuceanniu">注册</el-button>
      </el-form-item>
    </el-form>
    <el-button type="primary" @click.native="denglu" >登录页</el-button>
    <el-button type="primary" @click.native="zuce" >注册页</el-button>
  </div>
</template>

<script>
export default {
  name: 'Signin',
  data () {
    var checkEmail=(rule,value,callback)=>{
      var reg=/^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
      var jy=reg.test(value);
      if(!jy){
        if(this.jy1){
          this.jy1=false;
          this.biaoji--;
        }
        callback(new Error('格式有误'))
      }else{
        if(!this.jy1){
          this.jy1=true;
          this.biaoji++;
        }
        console.log(this.biaoji);
        callback()
      }
    };
    var checkNumber=(rule,value,callback)=>{
      var reg=/^[0-9]{6,10}$/
      var jy=reg.test(value);
      if(!jy){
        if(this.jy2){
          this.jy2=false;
          this.biaoji--;
        }
        callback(new Error('格式有误'))
      }else{
        if(!this.jy2){
          this.jy2=true;
          this.biaoji++;
        }
        callback()
      }
    };
    return {
      activate: 1,
      form: {
          username: '',
          password: ''
      },
      activeIndex:'1',
      biaoji:0,
      status:-1,
      rules: {
      username: [
        {validator:checkEmail, message:'请输入正确的邮箱',trigger:'blur'},
      ],
      password: [
        {validator: checkNumber, message: '请输入正确的密码(6-10位数字)', trigger: 'blur'}
      ]
    },
    }
  },
  methods:{
    submit:function(){
    //把mailbox，password发送给后端
    //后端返回状态字
    //0：注册成功，待激活
    //1:账号已存在
    //2：发送邮件失败
    this.postData();
    },
    denglu:function(){
    this.$router.push('/signin');
    },
    postData:function(){
  //把mailbox，password发送给后端,并获得返回状态字
  this.$http.post(this.store2.state.basicUrl + 'register/',{username:this.form.username,password:this.form.password},{emulateJSON:true}).then(function(res){
      this.status = res.body.status;
      console.log(res.body.status);
      if (this.status == 0) {
        this.$router.push('/signin')
      }
  },function(err){
  console.log(err);
  });
  },
  deactivate:function(){
    this.$http.get(this.store2.state.basicUrl + 'activate/<activate_id>').then(function(res){
                    if (res.body.status)
                      console.log('激活失败');
                    else  
                      activate = 0;
                },function(){
                    console.log('请求失败处理');
                })
  },
  zuce:function(){
    console.log("!");
    this.$router.push('/register');
  },
  false_deactivate:function (){
    alert("未正确填写必要信息");
  },
  false_submit:function (){
    alert("未激活");
  }
  }
}
</script>

<style scoped>
.buhuanhang{
  display:inline
}
.login-box {
    border: 1px solid #DCDFE6;
    width: 350px;
    margin: 180px auto 20px auto;
    padding: 35px 35px 15px 35px;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    box-shadow: 0 0 25px #909399;
  }
.login-title {
    text-align: center;
    margin: 0 auto 20px auto;
    color: #303133;
  }
#daohang{
  margin-top: -150px;
  font-size: 24px;
}
#denglukuan {
  margin-top: 20px;
}
.zuceanniu{
  float: right;
}
</style>
