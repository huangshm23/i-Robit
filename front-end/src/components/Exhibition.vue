<template>
  <div id="exhibition">
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
    <div id="position">
      <div v-if="riskVisiable" class="msg">{{msg1}}</div>
      <div v-else class="msg">{{msg2}}</div>
      <div id="charts">
        <ve-pie :data="chartData" :settings="chartSettings"></ve-pie>
      </div>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card v-if="riskVisiable" shadow="hover"  body-style="padding:10px">
            <div slot="header" class="clearfix">预期收益率</div>
            {{this.$store.state.combination.expected_rate}}
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card  v-if="riskVisiable" shadow="hover" body-style="padding:10px">
            <div slot="header" class="clearfix">风险等级</div>
            {{this.$store.state.combination.risk_factor}}
          </el-card>
        </el-col>
        <el-col :span="8" id="step">
          <el-card shadow="hover" body-style="padding:0px">
            <div slot="header" class="clearfix">步长</div>
            <el-input-number v-model="step" :min="0" :max="0.1" :precision="2" :step="0.01"></el-input-number>
          </el-card>
        </el-col>
      </el-row>
      <div id="table">
        <el-table :data="this.$store.state.combination.recommendation" border >
          <el-table-column type="index" ></el-table-column>
          <el-table-column prop="name" label="名称" min-width="80%"></el-table-column>
          <el-table-column >
            <template slot="header">比例</template>
            <template slot-scope="scope">
              <el-input-number v-model="scope.row.ratio" @change="(newval,oldval) => handleChange(newval,oldval,scope.$index)" :min="0" :max="1" :precision="4" :step="step"></el-input-number>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <el-button type="success" @click="simulation">模 拟</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Exhibition',
  data(){
    this.chartSettings = {
        dimension: 'name',
        metrics: 'ratio'
    }
    return{
        msg1:"推荐的组合",
        msg2:"自定义组合",
        step:0.05,
        riskVisiable:true,
        rateVisiable:true,
        activeIndex:'1',
        chartData: {
          columns: ['name', 'ratio'],
          rows: []
        }
    }
  },
  methods:{
      logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
      //发送退出请求到后端，返回0成功, 1失败
      this.$http.get(this.$store2.state.basicUrl + 'logout/').then(function(res){
                    if (res.body.status)
                      console.log('退出失败'); 
                },function(){
                    console.log('请求失败处理');
                });
    },
    simulation:function(){
        //把基金种类发送给后端，得到预期收益，赋值给msg
    this.$http.post(this.$store.state.basicUrl + 'simulation/?token=' + this.$store.state.token,{
        'fund_ratio': this.$store.state.combination.recommendation
    },{emulateJSON:true}).then(function(res){
      msg = "预期收益率： " + res.body.expected_rate;
      },function(err){
      console.log(err);
      });
    },
    handleChange:function(newval,oldval,index){
      var s=newval-oldval
      var len=this.$store.state.combination.recommendation.length;
      this.riskVisiable=false;
      this.rateVisiable=false;
      for(var i=0;i<len;i++){
        this.$store.state.combination.recommendation[i].ratio*=1/(1+s);
      }
    }
  },
  mounted:function(){
    this.step=0.01*(this.$store.state.combination.recommendation.length-1);
    this.chartData.rows=this.$store.state.combination.recommendation;
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
  padding-bottom: 20px;
  min-height: 500px;
}
#table{
  margin: 10px;
}
#step{
  float: right;
}
.msg{
  font-size: 30px;
  color: #284EA5;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
