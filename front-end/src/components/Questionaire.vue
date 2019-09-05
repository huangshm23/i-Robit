<template>
  <div class="register">
    <router-link :to="{ path: '/recommendation' }">组合推荐</router-link>
    <router-link :to="{ path: '/news' }">新闻推荐</router-link>
    <button @click="logout" class="buhuanhang">退出登录</button>
    <hr>
    <h1>Questionaire</h1>
    <div id="form" v-for="q in questions" :key="q.num">
      <div>{{q.num}}:{{q.question}}</div>
      <div v-for="o in q.options" :key="o.op">
          <input v-if="o.op=='A'" type="radio" :name="q.num" :value="o.op" checked=true @click="update(q.num,o.op)">
          <input v-else type="radio" :name="q.num" :value="o.op" @click="update(q.num,o.op)">
          {{o.op}}:{{o.option}}
      </div>
    </div>
      <button @click="submit">提交</button>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
  return {
  biaoji:0,
  questions:[
      {
        num:1,
        question:"在风险态度方面，朋友对您的评价最有可能是?",
        options:[
            {op:"A",option:"一个真正的赌博者"},
            {op:"B",option:"一个进行充分研究后愿意承担风险的人"},
            {op:"C",option:"一个小心谨慎的人"},
            {op:"D",option:"一个真正的风险规避者"}
        ],
      },
      {
        num:2,
        question:"假如您正在一个电视游戏节目中面临以下几个选择，您会选择哪一项?",
        options:[
          {op:"A",option:"100%的机会获得4,000元现金"},
          {op:"B",option:"50%的机会获得20,000元现金"},
          {op:"C",option:"25%的机会获得40,000元现金"},
          {op:"D",option:"5%的机会获得400,000元现金"}
        ]
      },
      {
        num:3,
        question:"假如您刚刚为一个千载难逢的好假期存够了旅行资金。在度假开始前的三个星期，您丢掉了自己的工作。您会：",
        options:[
          {op:"A",option:"取消这次度假"},
          {op:"B",option:"改成一次资金花费小很多的度假"},
          {op:"C",option:"按照原计划度假，您认为自己需要时间去准备寻找下一份工作"},
          {op:"D",option:"延长您的假期，因为这可能是您最后一次机会享受这么好的假期"}
        ]
      },
      {
        num:4,
        question:"假如您意外地收到80,000元可以用来投资，您会怎么做？",
        options:[
          {op:"A",option:"把钱存到储蓄账户里"},
          {op:"B",option:"投资于安全优质的债券或债券基金"},
          {op:"C",option:"投资于股票或股票基金"}
        ]
      },
      {
        num:5,
        question:"在投资体验方面，您投资股票或股票资金的时候感觉愉快吗?",
        options:[
          {op:"A",option:"并非总是愉快"},
          {op:"B",option:"比较愉快"},
          {op:"C",option:"非常愉快"}
        ]
      },
      {
        num:6,
        question:"对于“风险”这个词，您首先会联想到下面的哪一项?",
        options:[
          {op:"A",option:"损失"},
          {op:"B",option:"不确定性"},
          {op:"C",option:"机会"},
          {op:"D",option:"刺激"}
        ]
      },
      {
        num:7,
        question:"一些专家预测，黄金、珠宝、收藏品和房地产等资产（硬资产）的价格将会上涨；然而，债券价格可能会下跌，专家们倾向于认为政府债券相对安全。您现在大部分的投资资是高息政府债券。您会怎么做?",
        options:[
          {op:"A",option:"继续持有债券"},
          {op:"B",option:"卖掉债券，把拿到的钱一半存到储蓄账户里，另一半投资于硬资产"},
          {op:"C",option:"卖掉债券，把拿到的钱全部投资于硬资产"},
          {op:"D",option:"卖掉债券，把拿到的钱全部投资于硬资产，并再额外借钱去投资更多的硬资产"}
        ]
      },
      {
        num:8,
        question:"以下四个选项描述了某种投资可能面临的最好和最坏的情况，您更喜欢哪一种投资?",
        options:[
          {op:"A",option:"投资的最佳情况是800元收益，最坏情况是0元收益/损失"},
          {op:"B",option:"投资的最佳情况是3,200元收益，最坏情况是800元损失"},
          {op:"C",option:"投资的最佳情况是10,400元收益，最坏情况是3,200元损失"},
          {op:"D",option:"投资的最佳情况是19,200元收益，最坏情况是9,600元损失"}
        ]
      },
      {
        num:9,
        question:"假如您已经得到了4,000元，现在面临以下两种情形，您会选择：",
        options:[
          {op:"A",option:"100%的机会获得额外2,000元"},
          {op:"B",option:"50%的机会获得额外4,000元，50%的机会没有额外收获"}
        ]
      },
      {
        num:10,
        question:"假如您已经得到了8,000元，现在面临以下两种情形，您会选择：",
        options:[
          {op:"A",option:"100%的可能性损失2,000元"},
          {op:"B",option:"50%的可能性损失4,000元，50%的可能性什么也不损失"}
        ]
      },
      {
        num:11,
        question:"假如一位亲戚留给您一笔400,000元的遗产，并在遗嘱中规定，你将所有的钱都投资于下列选择之一。您会选择哪一个?",
        options:[
          {op:"A",option:"储蓄账户或货币基金"},
          {op:"B",option:"投资于股票和债券的混合基金"},
          {op:"C",option:"一个由15只普通股组成的投资组合"},
          {op:"D",option:"黄金、白银和石油等大宗商品"}
        ]
      },
      {
        num:12,
        question:"如果您需要投资80,000元，下面哪一项投资选择对您来说最有吸引力?",
        options:[
          {op:"A",option:"60%投资低风险资产，30%投资中等风险资产，20%投资高风险资产"},
          {op:"B",option:"30%投资低风险资产，40%投资中等风险资产，30%投资高风险资产"},
          {op:"C",option:"10%投资低风险资产，40%投资中等风险资产，50%投资高风险资产"}
        ]
      },
      {
        num:13,
        question:"有一位您信任的邻居兼朋友，他是一位经验丰富的地质学家，正在组织一群投资者为开发一个油井集资。这是一次投资冒险，如果成功，它将带来50~100倍的投资收益；如果失败，则所有的投资都一文不值。您的朋友估计成功的概率只有20%，如果您有资金可供投资这个项目，您会投资多少?",
        options:[
          {op:"A",option:"不投资"},
          {op:"B",option:"一个月的工资"},
          {op:"C",option:"三个月的工资"},
          {op:"D",option:"六个月的工资"}
        ]
      }
  ]
  }
  },
  methods:{
    submit:function(){
    //把result发给后端，根据返回结果：1转移到组合展示页，2弹出警告
    this.$http.post('http://129.211.63.182:80/recommendate/',{'questionnaire': 
        this.$store.state.result[0] + ',' +
        this.$store.state.result[1] + ',' +
        this.$store.state.result[2] + ',' +
        this.$store.state.result[3] + ',' +
        this.$store.state.result[4] + ',' +
        this.$store.state.result[5] + ',' +
        this.$store.state.result[6] + ',' +
        this.$store.state.result[7] + ',' +
        this.$store.state.result[8] + ',' +
        this.$store.state.result[9] + ',' +
        this.$store.state.result[10] + ',' +
        this.$store.state.result[11] + ',' +
        this.$store.state.result[12]       
    },{emulateJSON:true}).then(function(res){
      //res.body.recommendation
      this.$store2.commit("updateRate",res.body.expected_rate,res.body.risk_factor);
      var myObj = res.body.recommendation;
      for (x in myObj) {
        this.$store2.commit("updateFund",x,myObj[x]);
      }
      this.$router.push('/exhibition')
      },function(err){
      console.log(err);
      });
    },
    update:function(a,b){
      var n={num:a-1,value:b}
      this.$store.commit("update",n)
    },
    logout:function(){
      this.$store.state.is_login=false
      this.$router.push('/')
      //发送退出请求到后端，返回0成功, 1失败
      this.$http.get('http://129.211.63.182:80/logout/?token=' + this.$store.token).then(function(res){
                    if (res.body.status == 1)
                      console.log('退出失败'); 
                },function(){
                    console.log('请求失败处理');
                });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="">
.buhuanhang{
  display:inline
}
</style>